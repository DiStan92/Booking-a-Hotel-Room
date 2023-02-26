from django.db import models
from users.models import User


class Room(models.Model):
    number = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    places = models.IntegerField()

    def __str__(self):
        return f"{self.pk} - {self.number}"

    class Meta:
        verbose_name = "number"
        verbose_name_plural = "numbers"


class Booking(models.Model):
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.SET_NULL, null=True)
    date_on = models.DateField(null=False)
    date_off = models.DateField(null=False)

    def __str__(self):
        return f"{self.pk} - {self.room}"

    class Meta:
        verbose_name = "booking"
        verbose_name_plural = "bookings"