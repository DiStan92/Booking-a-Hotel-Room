from django.db import models

class Room(models.Model):
    number = models.IntegerField()
    price = models.DecimalField(max_digits=5, decimal_places=2)
    places = models.IntegerField()

    def __str__(self):
        return f'{self.pk} - {self.number}'

    class Meta:
        verbose_name = 'number'
        verbose_name_plural = 'numbers'
