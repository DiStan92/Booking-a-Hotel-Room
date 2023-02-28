from django.urls import path, re_path

from .endpoints import BookingLCView, RegistrUserView

urlpatterns = [
    path("registr/", RegistrUserView.as_view(), name="registr"),
    re_path("^guest/(?P<id>.+)/booking", BookingLCView.as_view(), name="user-booking"),
]
