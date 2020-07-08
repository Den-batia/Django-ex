from django.contrib import admin
from django.urls import path, include
from rest_framework import routers
from app import views
from app.yasg import urlpatterns as sd_url

router = routers.DefaultRouter()
router.register(r'users', views.UserViewSet)
router.register(r'news', views.NewsViewSet)

urlpatterns = [
    path('admin/', admin.site.urls),
    # path('', include(router.urls)),
    # path('accounts/', include('allauth.urls')),
    # path('captcha/', include('captcha.urls')),
    # path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/register/', views.Register.as_view(), name='register'),
    path('accounts/login/', views.Login.as_view(), name='login'),
    path('confirm_register/<str:uuid>/', views.Confirm_Registration.as_view(), name='confirm_registration'),
    path('logout/', views.LogOut.as_view(), name='logout'),
    path('auth/', include('djoser.urls')),
    path('auth/', include('djoser.urls.authtoken')),
    path('', views.App_Index.as_view(), name='index'),
    # path('login/', views.Login.as_view(), name='login'),


    path('api/', include('app.urls')),
]
urlpatterns += sd_url

