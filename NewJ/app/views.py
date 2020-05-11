from django.core.exceptions import ImproperlyConfigured
from django.shortcuts import render
from .models import Man
from .forms import *
from django.http import HttpResponse, HttpRequest
from django.views.generic import CreateView, FormView, UpdateView
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


class App_Index(CreateView):
    form_class = MenForm
    model = Man
    template_name = 'app/index.html'
    success_url = reverse_lazy('index')

    def get_context_data(self, **kwargs):
        obj = self.model.objects.all()
        kwargs['obj'] = obj
        return super().get_context_data(**kwargs)


#
# class A(CreateView):
#     # model = Man
#
#     form_class = MenForm
#     success_url = reverse_lazy('index')
#     template_name = 'app/create_Men.html'



class Register(CreateView):
    # model = User
    template_name = 'app/register.html'
    form_class = RegisrerForm
    success_url = reverse_lazy('index')

class LogOut(LogoutView):
    next_page = reverse_lazy('login')
    template_name = 'app/logout.html'

class B(FormView):
    form_class = MenForm
    template_name = 'app/b.html'

class C(UpdateView):
    model = Man
    template_name = 'app/detail.html'
    form_class = MenForm

    def get(self, request, *args, **kwargs):
        self.object = self.get_object()

        if str(request.user) == self.object.name:
            return super().get(request, *args, **kwargs)
        else:
            raise Http404('Вы не имеете права к указанному посту!!!')






