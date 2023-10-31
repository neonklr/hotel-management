# Create your views here.
from django.shortcuts import render, HttpResponse, redirect
from users.models import User

def update_profile(request, user=None):
    if request.method  == "GET":
        if user:
            return render(request, "update.html", {"user": user})
        return HttpResponse("<h3>direct access forbidden</h3>")
    
    elif request.method == "POST":
        return update_profile_logic(request)


def view_profile(request, user=None):
    if user:
        return render(request, "view.html", {"user": user})
    
    return HttpResponse("<h3>direct access forbidden</h3>")


def update_profile_logic(request):
    data = {
        "name": request.POST["name"],
        "email" : request.POST["email"],
        "password" : request.POST["password"],
        "date_of_birth" : request.POST["DateOfBirth"],
        "phone_number" : request.POST["phoneNumber"],
        "address" : request.POST["Address"]
    }

    for key, value in data.items():
        if not value:
            return redirect("/user/update")

    User(**data).save()
    return redirect("/dashboard")
