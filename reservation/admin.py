# Register your models here.
from django.contrib import admin

from reservation.models import Reservation, Room

admin.site.register(Reservation)
admin.site.register(Room)
