# Create your views here.
from django.contrib import messages
from django.shortcuts import redirect, render

from authentication.logic import auth
from user.models import User


@auth(by_pass_route=True)
def update_profile(request):
    if request.method == "GET":
        if request.user:
            return render(request, "update.html", {"user": request.user})

        messages.error(request, "You are not authorized to view this page.")
        return redirect("/dashboard")

    elif request.method == "POST":
        return update_profile_logic(request)


@auth()
def view_profile(request):
    if request.user:
        return render(request, "view.html", {"user": request.user})

    messages.error(request, "You are not authorized to view this page.")
    return redirect("/dashboard")


@auth(by_pass_route=True)
def update_profile_logic(request):
    data = {
        "name": request.POST["name"],
        "email": request.POST["email"],
        "password": request.POST["password"],
        "date_of_birth": request.POST["DateOfBirth"],
        "phone_number": request.POST["phoneNumber"],
        "address": request.POST["Address"],
    }

    for key, value in data.items():
        if not value:
            return redirect("/user/update")

    User(**data).save()
    return redirect("/dashboard")
