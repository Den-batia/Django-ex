from django.shortcuts import render
from .models import Man
from .forms import *
from django.http import HttpResponse, HttpRequest
from django.views.generic import CreateView
from django.urls import reverse_lazy

from django.views.generic import View

# Create your views here.
class Login(View):
    def get(self, request):
        l = LoginFornm()
        return render(request, 'app/login.html', context={'l': l})
    def post(self, reqest):
        l = LoginFornm(reqest.POST)

        if l.is_valid():
            # print(f.save())
            return HttpResponse('учетная запись создана')
        else:
            return render(reqest, 'app/login.html', context={'l': l})


def index(request):
    print('11111')
    # a = Man.ob
    return HttpResponse('ddddddddddd')

class A(View):
    def get(self, request):
        obj = Man.objects.all()
        f = MenForm()
        return render(request, 'app/create_Men.html', context={'f': f, 'obj': obj})

    def post(self, request):
        f = MenForm(request.POST)
        print(f.errors)
        if f.is_valid():
            print(f.save())
            return HttpResponse('учетная запись создана')
        else:
            return render(request, 'app/create_Men.html', context={'f': f})

class Register(CreateView):
    model = User
    template_name = 'app/register.html'
    form_class = RegisrerForm
    success_url= reverse_lazy('create')
