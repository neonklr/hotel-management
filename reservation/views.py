# # Create your views here.
from datetime import datetime

from django.contrib import messages
from django.shortcuts import redirect, render

from authentication.logic import auth

from . import logic
from .models import Reservation, ReservationStatus


@auth()
def view_reservation(request):
    user_reservations = Reservation.objects.filter(guest=request.user).order_by("booked_on")
    return render(
        request, "reservation/view.html", {"reservations": user_reservations, "ReservationStatus": ReservationStatus}
    )


# Cancels reservations if user is logged in and validated.
@auth()
def cancel_reservation(request, uuid):
    resv = Reservation.objects.get(uuid=uuid)

    if resv.guest != request.user:
        messages.error(request, "You are not authorized to cancel this reservation.")
        return redirect("/dashboard")

    resv.cancel()
    messages.success(request, "Reservation cancelled successfully.")
    return redirect("/reservation/view")


@auth()
def new_reservation(request):
    if request.method == "GET":
        return render(request, "reservation/new.html")

    elif request.method == "POST":
        start_datetime_str = request.POST.get("checkIn")
        end_datetime_str = request.POST.get("checkOut")

        start_time, end_time = logic.get_start_end_datetime(start_datetime_str, end_datetime_str)

        if (start_time < datetime.now()) or (end_time < datetime.now()):
            messages.error(request, "Please select a future date.")
            return redirect("/reservation/new")

        if start_time >= end_time:
            messages.error(request, "Check out date must be after check in date.")
            return redirect("/reservation/new")

        available_rooms = logic.calculate_available_rooms(start_time, end_time)
        available_rooms_count = {room_type: len(rooms) for room_type, rooms in available_rooms.items()}

        return render(
            request,
            "reservation/new.html",
            {"room_type_counts": available_rooms_count, "checkIn": start_datetime_str, "checkOut": end_datetime_str},
        )


@auth()
def checkout_room(request, uuid):
    resv = Reservation.objects.get(uuid=uuid)

    if resv.guest != request.user:
        messages.error(request, "You are not authorized to checkout this reservation.")
        return redirect("/dashboard")

    resv.checked_out_at = datetime.now()
    resv.status = ReservationStatus.checked_out_refund_pending
    resv.save()

    return redirect("/reservation/view")


# Logic for booking rooms
@auth()
def book_room(request):
    if request.method == "POST":
        roome_type = request.POST.get("roomType")

        start_datetime, end_datetime = logic.get_start_end_datetime(
            request.POST.get("checkIn"), request.POST.get("checkOut")
        )

        room = logic.calculate_available_rooms(start_datetime, end_datetime)[roome_type][0]

        no_of_days = (end_datetime - start_datetime).days

        if (end_datetime - start_datetime).seconds > 0:
            no_of_days += 1

        if no_of_days > 0:
            resv = Reservation(
                guest=request.user,
                booked_on=datetime.now(),
                booked_from=start_datetime,
                booked_to=end_datetime,
                room=room,
                payment_amount=no_of_days * room.price,
                status=ReservationStatus.booked_payment_due,
            )

            room.save()
            resv.save()

            return redirect("/reservation/view")
        else:
            messages.error(request, "Please fill in all the details ...")
            return redirect("/reservation/new")
