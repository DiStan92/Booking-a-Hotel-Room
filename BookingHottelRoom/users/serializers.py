from rest_framework import serializers

from .models import Booking, User

__all__ = ["UserRegistrSerializer", "BookingSerializer"]


class UserRegistrSerializer(serializers.ModelSerializer):
    password2 = serializers.CharField()

    class Meta:
        model = User
        fields = ["email", "username", "password", "password2"]

    def save(self, *args, **kwargs):
        user = User(
            email=self.validated_data["email"],
            username=self.validated_data["username"],
        )

        password = self.validated_data["password"]
        password2 = self.validated_data["password2"]
        if password != password2:
            raise serializers.ValidationError({password: "Password does not match"})
        user.set_password(password)
        user.save()
        return user


class BookingSerializer(serializers.ModelSerializer):
    class Meta:
        model = Booking
        fields = "__all__"
