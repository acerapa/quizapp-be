from django.urls import path

from rest_framework_simplejwt.views import TokenRefreshView, TokenVerifyView, TokenBlacklistView

from . import views

urlpatterns = [
    path('me', views.user, name='api_user'),
    path('register', views.register, name='api_register'),
    path('token', views.CustomTokenObtainPairView.as_view(), name='api_token_auth'),
    path('token/verify', TokenVerifyView.as_view(), name='api_token_verify'),
    path('token/refresh', TokenRefreshView.as_view(), name='api_token_refresh'),
    path('token/blacklist', TokenBlacklistView.as_view(), name='api_token_blacklist'),
]
