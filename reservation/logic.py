from datetime import datetime

from .models import Reservation, Room


def calculate_available_rooms(start_time, end_time):
    available_rooms = {}

    for room in Room.objects.all():
        conflicting_reservations = Reservation.objects.filter(
            room=room, booked_from__lt=end_time, booked_to__gt=start_time
        )

        if not conflicting_reservations.exists():
            if available_rooms.get(room.type) is None:
                available_rooms[room.type] = [room]
            else:
                available_rooms[room.type].append(room)

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
