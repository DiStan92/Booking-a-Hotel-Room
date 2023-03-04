from django.contrib.auth.models import AbstractUser, PermissionsMixin
from django.db import models
from django.utils.translation import gettext_lazy as _

from room.models import Room

__all__ = ["User", "Booking"]


class User(AbstractUser, PermissionsMixin):
    def __str__(self):
        return f"{self.pk} - {self.email}"

    class Meta:
        verbose_name = _("user")
        verbose_name_plural = _("users")


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_start_at = models.DateField(null=False)
    date_end_at = models.DateField(null=False)

    def __str__(self):
        return f"{self.pk} - {self.guest} - {self.room}"

    class Meta:
        verbose_name = "booking"
        verbose_name_plural = "bookings"
