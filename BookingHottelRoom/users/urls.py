from django.contrib import admin
from django.urls import include, path
from .endpoints import RegistrUserView

urlpatterns = [
    path('api-auth', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    path('registr/', RegistrUserView.as_view(), name='registr')
]