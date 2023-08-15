from django.urls import path

from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from . import views

urlpatterns = [
    path('', views.users, name='api_users'),
    path('register', views.register, name='api_register'),
    path('token', TokenObtainPairView.as_view(), name='api_token_auth'),
    path('token/verify', TokenVerifyView.as_view(), name='api_token_verify'),
    path('token/refresh', TokenRefreshView.as_view(), name='api_token_refresh'),
]
