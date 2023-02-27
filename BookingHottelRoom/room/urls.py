from django.urls import include, path

from .endpoints import RoomAPIView

urlpatterns = [path("", RoomAPIView.as_view(), name="room")]
