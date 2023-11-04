# Create your models here.
import uuid

from django.db import models

from user.models import User


class Room(models.Model):
    no = models.IntegerField(primary_key=True, unique=True)
    type = models.CharField(max_length=100)
    price = models.IntegerField()
    is_available = models.BooleanField(default=True)


class Reservation(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    booked_on = models.DateField()
    booked_from = models.DateTimeField()
    booked_to = models.DateTimeField()
    room = models.ForeignKey(Room, on_delete=models.CASCADE)
    guest = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20)
    payment_amount = models.IntegerField()
    checked_in_at = models.DateTimeField(null=True, blank=True)
    checked_out_at = models.DateTimeField(null=True, blank=True)
    status = models.CharField(max_length=100)

    def cancel(self):
        self.status = "Cancelled"
        self.room.is_available = True

        self.room.save()
        self.save()
