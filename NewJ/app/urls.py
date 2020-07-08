from django.contrib import admin
from django.urls import path, include
from .views import *
from .yasg import urlpatterns as yasg_url
from rest_framework import routers
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView


router = routers.DefaultRouter()
router.register(r'users', UserViewSet)
router.register(r'news', NewsViewSet)

urlpatterns = [
    path('', include(router.urls)),
    path('gettoken/', MyGetToken.as_view(), name='get_token'),
    path('token/', TokenObtainPairView.as_view(), name='token_obtain_pair'),
    path('token/refresh/', TokenRefreshView.as_view(), name='token_refresh'),
    path('token/verify/', TokenVerifyView.as_view(), name='token_verify'),

    # path('createNew/', A.as_view(), name='create'),
    # path('b/', B.as_view(), name='B'),
    path('<str:slug>/', C.as_view(), name='detail'),
    path('<str:pk>/authenticate/', My_Auth.as_view(), name='authenticate')
]
