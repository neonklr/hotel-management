# # Create your views here.
from datetime import datetime

from django.contrib import messages
from django.shortcuts import HttpResponse, redirect, render

from authentication.logic import auth
from user.models import User

from .models import Reservation, Room


def new_reservation_view(request):
    return render(request, "new.html")


def update_reservation_view(request):
    return render(request, "update.html")


# Cancels reservations if user is logged in and validated.
@auth()
def cancel_reservation(request, uuid):
    resv = Reservation.objects.get(uuid=uuid)
    if resv.email != User.objects.get(email=request.session.get("login_token")):
        messages.error(request, "You are not authorized to cancel this reservation.")
        return redirect("/")

    resv.completed = "Cancelled"
    resv.room_no.is_available = True
    resv.room_no.save()
    resv.save()
    messages.success(request, "Reservation cancelled successfully.")
    return redirect("/dashboard/")


@auth()
def room_list(request):
    if request.method == "GET":
        return render(request, "new.html")
    elif request.method == "POST":
        start_time_str = request.POST.get("checkIn")
        end_time_str = request.POST.get("checkOut")
        start_time = datetime.strptime(start_time_str, "%Y-%m-%d")
        end_time = datetime.strptime(end_time_str, "%Y-%m-%d")
        if (end_time - start_time).days < 0:
            available_rooms_count = 0
        else:
            available_rooms_count = calculate_available_rooms_by_room_type(start_time, end_time)
        return render(
            request,
            "new.html",
            {"room_type_counts": available_rooms_count, "checkIn": start_time_str, "checkOut": end_time_str},
        )


def calculate_available_rooms_by_room_type(start_time, end_time):
    available_rooms_count = {}

    room_types = Room.objects.values("room_type").distinct()
    for room_type in room_types:
        room_type_name = room_type["room_type"]
        rooms_of_type = Room.objects.filter(room_type=room_type_name)
        available_count = 0
        for room in rooms_of_type:
            reservations = Reservation.objects.filter(
                room_no=room, booked_from__gte=end_time, booked_to__lte=start_time
            )
            if not reservations.exists():
                available_count += 1
        available_rooms_count[room_type_name] = available_count
    return available_rooms_count


# Logic for booking rooms
def book_rooms(request):
    if request.method == "POST":
        room_type = request.POST.get("roomType")
        start_time_str = request.POST.get("checkIn")
        end_time_str = request.POST.get("checkOut")
        print(room_type)
        available_rooms = Room.objects.filter(is_available=True, room_type=room_type)
        room = available_rooms[0]
        no_of_days = (datetime.strptime(end_time_str, "%Y-%m-%d") - datetime.strptime(start_time_str, "%Y-%m-%d")).days
        if start_time_str and end_time_str:
            resv = Reservation(
                date=datetime.now(),
                email=User.objects.get(email=request.session.get("login_token")),
                booked_from=start_time_str,
                booked_to=end_time_str,
                room_no=room,
                payment_method="UPI / Online Payment",
                payment_amount=no_of_days * room.room_price,
                completed="No",
            )
            resv.save()
            room.is_available = False
            room.save()
            return redirect("/dashboard")
        else:
            return HttpResponse("Please fill in all the fields.")

    return render(request, "reservation/new.html")
