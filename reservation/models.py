# Create your models here.
from django.db import models
import uuid
from users.models import User
from rooms.models import Room


class Reservation(models.Model):
    uuid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    date = models.DateField()
    booked_from = models.DateTimeField()
    booked_to = models.DateTimeField()
    room_no = models.ForeignKey(Room, on_delete=models.CASCADE)
    email = models.ForeignKey(User, on_delete=models.CASCADE)
    payment_method = models.CharField(max_length=20)
    payment_amount = models.IntegerField()
    checked_out = models.BooleanField(default=False)
    completed = models.BooleanField(default=False)
