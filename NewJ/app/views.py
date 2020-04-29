from django.shortcuts import render
from .models import Man
from .forms import *
from django.http import HttpResponse
from django.views.generic import View

# Create your views here.
def index(request):
    print('11111')
    # a = Man.ob
    return HttpResponse('ddddddddddd')

class A(View):
    def get(self, request):
        f = MenForm()
        return render(request, 'app/create_Men.html', context={'f': f})

    def post(self, request):
        f = MenForm(request.POST)

        if f.is_valid():
            m = Man(f.cleaned_data)
            m.save()
            return HttpResponse('учетная запись создана')
        else:
            return render(request, 'app/create_Men.html', context={'f': f})