from django.contrib import admin
from django.urls import path, include
from .views import *

urlpatterns = [
    # path('createNew/', A.as_view(), name='create'),
    # path('b/', B.as_view(), name='B'),
    path('<str:slug>/', C.as_view(), name='detail'),
    path('<str:pk>/authenticate/', My_Auth.as_view(), name='authenticate')
]