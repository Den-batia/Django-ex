from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render
from .models import News
from .forms import *
from django.http import HttpResponse, HttpRequest
from django.views.generic import CreateView, FormView, UpdateView, DetailView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy
from django.views.generic import View
from django.http import Http404


# Create your views here.
class Login(LoginView):
    success_url = reverse_lazy('index')
    template_name = 'app/login.html'

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
        kwargs['obj'] = obj
        return super().get_context_data(**kwargs)





class Register(CreateView):
    # model = User
    template_name = 'app/register.html'
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
        obj = form.save(commit=False)
        obj.is_active = False
        obj.save()
        form.save_m2m()
        return super().form_valid(form)


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
