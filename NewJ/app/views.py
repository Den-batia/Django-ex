from django.shortcuts import render
from .models import Man
from .forms import *
from django.http import HttpResponse, HttpRequest
from django.views.generic import CreateView
from django.contrib.auth.views import LoginView, LogoutView
from django.urls import reverse_lazy

from django.views.generic import View


# Create your views here.
class Login(LoginView):
    success_url = reverse_lazy('index')
    template_name = 'app/login.html'
    def get_success_url(self):
        return self.success_url


class App_Index(CreateView):
    template_name = 'app/index.html'
    form_class = RegisrerForm


class A(View):
    def get(self, request):
        obj = Man.objects.all()
        f = MenForm()
        return render(request, 'app/create_Men.html', context={'f': f, 'obj': obj})

    def post(self, request):
        f = MenForm(request.POST)
        if f.is_valid():
            print(f.save())
            return HttpResponse('учетная запись создана')
        else:
            return render(request, 'app/create_Men.html', context={'f': f})


class Register(CreateView):
    model = User
    template_name = 'app/register.html'
    form_class = RegisrerForm
    success_url = reverse_lazy('create')

class LogOut(LogoutView):
    success_url = reverse_lazy('index')
    template_name = 'app/logout.html'
    def get_success_url(self):
        return self.success_url


