from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api_room/", include("room.urls")),
    path("api-auth", include("rest_framework.urls")),
    path("auth/", include("djoser.urls")),
    path("active/", include("users.urls")),
]
