from django.urls import include, path, re_path
from rest_framework.routers import DefaultRouter

from .endpoints import RoomViewSet

router = DefaultRouter()
router.register(r"room", RoomViewSet)

urlpatterns = [
    path("", include(router.urls)),
    #re_path()
]