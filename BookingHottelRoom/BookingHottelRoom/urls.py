from django.contrib import admin
from django.urls import include, path

urlpatterns = [
    path("admin/", admin.site.urls),
    path("room/", include("room.urls")),
    path("users/", include("users.urls")),
]
