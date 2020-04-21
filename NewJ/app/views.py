from django.shortcuts import render
from django.shortcuts import redirect
from django.http import HttpRequest
from django.http import HttpResponse
import time

# Create your views here.
def index(request):

    return render(request, 'app/index.html')

def a(request):
    if request.method == 'POST':
        print(request.POST)
        return redirect(index)
    return render(request, 'app/a.html')