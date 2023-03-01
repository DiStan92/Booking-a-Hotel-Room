from django.urls import path

from .endpoints import RoomAPIView, RoomListView

urlpatterns = [path("", RoomAPIView.as_view(), name="room"), path("room-filter", RoomListView.as_view(), name="room-filter")]
