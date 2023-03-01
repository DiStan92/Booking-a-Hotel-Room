from django.urls import include, path, re_path
from rest_framework import routers
from rest_framework.routers import DefaultRouter

from .endpoints import BookingLCView, BookingViewSet, RegistrUserView

router = DefaultRouter()
router.register("booking-viewset", BookingViewSet)

urlpatterns = [
    path("", include((router.urls, "booking"))),
    path("registr/", RegistrUserView.as_view(), name="registr"),
    re_path("^guest/(?P<id>.+)/booking", BookingLCView.as_view(), name="user-booking"),
]
