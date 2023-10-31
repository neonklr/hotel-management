
from rooms.models import Room

def check_availability(request):
    available_rooms = Room.objects.filter(
        is_available=True
    ).values_list('room_no', flat=True)
    selected_room = request.GET.get('room_no')
    if selected_room in available_rooms:
        return True
    return False