from rest_framework import permissions
from rest_framework.generics import ListAPIView
from .models import Room
from .serializers import RoomSerializer

class RoomAPIView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer
    permission_classes = [permissions.AllowAny]
