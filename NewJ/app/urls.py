from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    path('', index, name='index'),
    path('a/createNew/', A.as_view(), name='create')
]