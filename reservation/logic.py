from datetime import datetime

from django.db.models import Q

from .models import Reservation, ReservationStatus, Room


def calculate_available_rooms(start_time, end_time):
    available_rooms = {}

    conflicting_rooms = Reservation.objects.filter(
        Q(booked_from__lt=end_time)
        & Q(booked_to__gt=start_time)
        & Q(status__in=[ReservationStatus.booked, ReservationStatus.booked_payment_due, ReservationStatus.checked_in])
    ).values_list("room", flat=True)

    for room in Room.objects.all():
        if room.no in conflicting_rooms:
            continue

        if available_rooms.get(room.type) is None:
            available_rooms[room.type] = set([room])
        else:
            available_rooms[room.type].add(room)

    return available_rooms


def get_start_end_datetime(start_datetime_str, end_datetime_str):
    try:
        start_datetime = datetime.strptime(start_datetime_str, "%Y-%m-%d")
    except ValueError:
        start_datetime = datetime.strptime(start_datetime_str, "%Y-%m-%d %H:%M:%S")

    try:
        end_datetime = datetime.strptime(end_datetime_str, "%Y-%m-%d")
    except ValueError:
        end_datetime = datetime.strptime(end_datetime_str, "%Y-%m-%d %H:%M:%S")

    return start_datetime, end_datetime
