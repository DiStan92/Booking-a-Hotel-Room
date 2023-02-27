from django.urls import path, re_path

from .endpoints import BookingRUDView, RegistrUserView

urlpatterns = [
    path("registr/", RegistrUserView.as_view(), name="registr"),
    re_path("^guest/(?P<id>.+)/booking", BookingRUDView.as_view(), name="user-booking"),
]
