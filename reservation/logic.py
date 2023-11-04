from .models import Reservation, Room


def calculate_available_rooms_by_room_type(start_time, end_time):
    available_rooms_count = {}
    room_types = Room.objects.values("type").distinct()

    for room_type in room_types:
        room_type_name = room_type["type"]
        rooms_of_type = Room.objects.filter(type=room_type_name)
        available_count = 0

        for room in rooms_of_type:
            reservations = Reservation.objects.filter(room=room, booked_from__gte=end_time, booked_to__lte=start_time)

            if not reservations.exists():
                available_count += 1

        available_rooms_count[room_type_name] = available_count
    return available_rooms_count
