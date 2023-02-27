from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api_room/", include("room.urls")),
    #path("api_users/", include("users.urls")),
    path('api-auth', include('rest_framework.urls')),
    path('auth/', include('djoser.urls')),
    #path('registr/', RegistrUserView.as_view(), name='registr')
]
