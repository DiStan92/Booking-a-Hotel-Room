from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import permissions, status
from rest_framework.generics import CreateAPIView, ListAPIView, ListCreateAPIView
from rest_framework.response import Response
from rest_framework.viewsets import ModelViewSet

from .models import Booking, User
from .serializers import BookingSerializer, UserRegistrSerializer


class RegistrUserView(CreateAPIView):
    queryset = User.objects.all()
    serializer_class = UserRegistrSerializer
    permission_classes = [permissions.IsAuthenticated]

    def post(self, request, *args, **kwargs):
        serializer = UserRegistrSerializer(data=request.data)
        data = {}
        if serializer.is_valid():
            serializer.save()
            data["response"] = True
            return Response(data, status=status.HTTP_200_OK)
        else:
            data = serializer.errors
            return Response(data)


class BookingLCView(ListAPIView):
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]

    def get_queryset(self):
        guest = self.kwargs["id"]
        return Booking.objects.filter(guest_id=guest)


class BookingListView(ListCreateAPIView):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]
    filter_backends = [DjangoFilterBackend]
    filterset_fields = ["date_on", "date_off"]


class BookingViewSet(ModelViewSet):
    queryset = Booking.objects.all()
    serializer_class = BookingSerializer
    permission_classes = [permissions.IsAuthenticated]
