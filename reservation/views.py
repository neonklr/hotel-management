# # Create your views here.
from datetime import datetime

from django.contrib import messages
from django.shortcuts import redirect, render

from authentication.logic import auth

from . import logic
from .models import Reservation, Room


def previous_reservation(request):
    return render(request, "history.html")


# Cancels reservations if user is logged in and validated.
@auth()
def cancel_reservation(request, uuid):
    resv = Reservation.objects.get(uuid=uuid)

    if resv.guest != request.user:
        messages.error(request, "You are not authorized to cancel this reservation.")
        return redirect("/dashboard")

    resv.cancel()
    messages.success(request, "Reservation cancelled successfully.")
    return redirect("/reservation/history")


@auth()
def new_reservation(request):
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
            available_rooms_count = logic.calculate_available_rooms_by_room_type(start_time, end_time)

        return render(
            request,
            "new.html",
            {"room_type_counts": available_rooms_count, "checkIn": start_time_str, "checkOut": end_time_str},
        )


# Logic for booking rooms
@auth()
def book_room(request):
    if request.method == "POST":
        room_type = request.POST.get("roomType")
        start_time_str = request.POST.get("checkIn")
        end_time_str = request.POST.get("checkOut")

        available_rooms = Room.objects.filter(is_available=True, type=room_type)
        room = available_rooms[0]

        no_of_days = (
            datetime.strptime(end_time_str, "%Y-%m-%d") - datetime.strptime(start_time_str, "%Y-%m-%d")
        ).days + 1

        if no_of_days > 0:
            resv = Reservation(
                guest=request.user,
                booked_on=datetime.now(),
                booked_from=start_time_str,
                booked_to=end_time_str,
                room=room,
                payment_amount=no_of_days * room.price,
                status="Payment Due",
            )

            room.is_available = False
            room.save()
            resv.save()

            return redirect("/reservation/history")
        else:
            messages.error(request, "Please fill in all the details ...")
            return redirect("/reservation/new")
