# Create your views here.
from django.contrib import messages
from django.shortcuts import redirect, render

from authentication.logic import auth
from user.models import User


@auth(by_pass_route=True)
def update_profile(request):
    if request.method == "GET":
        if request.user:
            return render(
                request,
                "user/update.html",
                {
                    "user": request.user,
                    "date_of_birth": request.user.date_of_birth.strftime("%Y-%m-%d")
                    if request.user.date_of_birth
                    else "",
                },
            )

        messages.error(request, "You are not authorized to view this page.")
        return redirect("/dashboard")

    elif request.method == "POST":
        return update_profile_logic(request)


@auth()
def view_profile(request):
    if request.user:
        return render(
            request,
            "user/view.html",
            {"user": request.user, "date_of_birth": request.user.date_of_birth.strftime("%Y-%m-%d")},
        )

    messages.error(request, "You are not authorized to view this page.")
    return redirect("/get_started/")


@auth(by_pass_route=True)
def update_profile_logic(request):
    data = {
        "name": request.POST["name"],
        "date_of_birth": request.POST["DateOfBirth"],
        "phone_number": request.POST["phoneNumber"],
        "address": request.POST["Address"],
    }

    for value in data.values():
        if not value:
            messages.error(request, "Please fill all the fields.")
            return redirect("/user/update/")

    user = User.objects.get(email=request.user.email)
    user.name = data["name"]
    user.date_of_birth = data["date_of_birth"]
    user.phone_number = data["phone_number"]
    user.address = data["address"]
    user.save()

    messages.success(request, "Profile updated successfully.")
    return redirect("/user/view/")
