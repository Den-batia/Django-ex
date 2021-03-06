from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render
from .models import News, My_User
from .forms import *
from . import tasks
from django.http import HttpResponse, HttpRequest
from django.views.generic import CreateView, FormView, UpdateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.sessions.models import Session
from django.urls import reverse_lazy
from django.views.generic import View
from django.http import Http404, HttpResponseRedirect
from django.core.mail import send_mail
from rest_framework import viewsets, permissions, renderers
from .serializers import MyUserSerializer, NewsSerializer
from rest_framework.decorators import api_view, throttle_classes
from rest_framework.throttling import UserRateThrottle
from rest_framework.response import Response
from rest_framework_simplejwt.tokens import RefreshToken

# Create your views here.
class Login(LoginView):
    success_url = reverse_lazy('index')
    template_name = 'registration/login.html'
    form_class = LoginFornm

    def get_success_url(self):
        return self.success_url

    def get_form_kwargs(self):
        kwargs = {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
        }

        if self.request.method in ('POST', 'PUT'):
            data = self.request.POST.copy()
            if data.get('username'):
                data['username'] = data['username'].lower()

            kwargs.update({
                'data': data,
                'files': self.request.FILES,
            })
        kwargs['request'] = self.request
        return kwargs


class App_Index(CreateView):
    form_class = NewsForm
    model = News
    template_name = 'app/index.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        obj = self.model.objects.all()
        # a = tasks.asd.delay(10)
        # kwargs['obj'] = obj
        # if not self.request.session.exists(self.request.session.session_key):
        #     self.request.session.create()
        # self.request.session['s'] = 's'
        # s = Session.objects.get(pk = self.request.session.session_key)
        # print(s.get_decoded())

        return super().get_context_data(**kwargs)


class Register(CreateView):
    model = My_User
    template_name = 'registration/register.html'
    form_class = RegisrerForm
    success_url = reverse_lazy('index')


    def get_form_kwargs(self):
        """Return the keyword arguments for instantiating the form."""
        kwargs = {
            'initial': self.get_initial(),
            'prefix': self.get_prefix(),
        }
        if self.request.method in ('POST', 'PUT'):
            data = self.request.POST.copy()
            if data.get('username'):
                data['username'] = data['username'].lower()

            kwargs.update({
                'data': data,
                'files': self.request.FILES,
            })

        if hasattr(self, 'object'):
            kwargs.update({'instance': self.object})
        return kwargs

    def form_valid(self, form):
        """If the form is valid, save the associated model."""
        for a in form.fields:
            print(dir(form.fields[a]))
        self.object = form.save(commit=False)
        self.object.is_active = False
        self.object.save()
        form.save_m2m()
        link = self.request.build_absolute_uri(self.object.get_absolute_url())
        send_mail(
            'Subject here',
            link,
            'denis.batia004@gmail.com',
            [self.object.email],
            fail_silently=False,
        )
        return HttpResponseRedirect(self.get_success_url())

class Confirm_Registration(DetailView):
    queryset = My_User.objects.all()
    template_name = 'app/b.html'


    def get(self, request, *args, **kwargs):
        self.object = self.get_object()
        context = self.get_context_data(object=self.object)
        return self.render_to_response(context)

    def get_object(self, queryset=None):

        uuid = self.kwargs.get('uuid')
        queryset = self.queryset.filter(uuid=uuid)
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
            if not obj.is_active:
                obj.is_active = True
                obj.save()
        except queryset.model.DoesNotExist:
            raise Http404(_("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})
        return obj


class My_Auth(View):

    model = AuthCode
    form_class = AuthForm
    template_name = 'app/authenticate.html'

    def get(self, request, *args, **kwargs):
        pk = kwargs.get('pk')
        queryset = None
        if queryset is None:
            queryset = self.model.objects.all()

        if pk is not None:
            queryset = queryset.filter(user=pk)

        # Next, try looking up by slug.
        if pk is None:
            raise AttributeError(
                "Generic detail view %s must be called with either an object "
                "pk in the URLconf." % self.__class__.__name__
            )
        try:
            # Get the single item from the filtered queryset
            obj = queryset.get()
            form = self.form_class()
            return render(request, 'app/authenticate.html', context={'form': form, 'object': obj})
        except queryset.model.DoesNotExist:
            raise Http404(("No %(verbose_name)s found matching the query") %
                          {'verbose_name': queryset.model._meta.verbose_name})



class LogOut(LogoutView):
    next_page = reverse_lazy('login')
    template_name = 'app/index.html'


class C(UpdateView):
    model = News
    template_name = 'app/detail.html'
    form_class = NewsForm
    success_url = reverse_lazy('index')

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if str(request.user) == self.object.name:
            return super().get(request, *args, **kwargs)
        else:
            raise Http404('Вы не имеете права к указанному посту!!!')


class MyGetToken(FormView):
    template_name = 'app/get_token.html'
    form_class = GetFormToken
    success_url = reverse_lazy('login')

    def get_form(self, form_class=None):
        if form_class is None:
            form_class = self.get_form_class()
        form = form_class(self.get_form_kwargs())
        return form

    def get(self, request, *args, **kwargs):
        if request.user.id:
            return self.render_to_response(self.get_context_data())
        return HttpResponseRedirect(self.get_success_url())

    def get_form_kwargs(self):
        kwargs = super().get_form_kwargs()
        if self.request.user.id:
            refresh = RefreshToken.for_user(self.request.user)
            kwargs.update({'refresh': str(refresh), 'access': str(refresh.access_token)})
            return kwargs



class UserViewSet(viewsets.ModelViewSet):

    queryset = User.objects.all().order_by('-date_joined')
    serializer_class = MyUserSerializer


class OncePerDayUserThrottle(UserRateThrottle):
    rate = '1/sec'


class NewsViewSet(viewsets.ModelViewSet):

    throttle_classes = (OncePerDayUserThrottle,)
    renderer_classes = (renderers.JSONRenderer,)
    queryset = News.objects.all()
    serializer_class = NewsSerializer
    permission_classes = (permissions.IsAuthenticated,)



