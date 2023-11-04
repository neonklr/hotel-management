# Create your models here.
from django.db import models


class Room(models.Model):
    room_no = models.IntegerField(primary_key=True, unique=True)
    room_type = models.CharField(max_length=100)
    room_price = models.IntegerField()
    is_available = models.BooleanField(default=True)
