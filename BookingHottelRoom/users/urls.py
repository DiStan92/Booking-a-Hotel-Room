from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .views import (
    BookingListAPIView,
    BookingListCreateAPIView,
    BookingViewSet,
    RegistrUserView,
)

router = DefaultRouter()
router.register("booking-viewset", BookingViewSet)

urlpatterns = [
    path("", include((router.urls, "booking"))),
    path("booking/", BookingListCreateAPIView.as_view(), name="user-booking"),
    path("registr/", RegistrUserView.as_view(), name="registr"),
    re_path("^guest/(?P<id>.+)/booking", BookingListAPIView.as_view(), name="user-booking"),
]
