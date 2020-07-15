from django.contrib import admin, sessions
from django.contrib.sessions.models import Session
from.models import *
from django.contrib.auth.models import User
# Register your models here.
admin.site.register(News)
admin.site.register(AuthCode)
admin.site.register(Session)