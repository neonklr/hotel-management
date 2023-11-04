# Create your views here.

from django.contrib import messages
from django.shortcuts import redirect

from user.models import User

from . import logic


def signup(request):
    if logic.get_session_data(request, "login_token"):
        return redirect("/dashboard")

    if request.method == "POST":
        email = request.POST.get("user_email")
        password = request.POST.get("user_password")
        repass = request.POST.get("repass")

        if not password == repass:
            messages.error(request, "Password does not match re-entered password")
            return redirect("/get_started#signup-tab-content")

        if User.objects.filter(email=email).exists():
            messages.error(request, "You are already registered... please login again")
            return redirect("/get_started#login-tab-content")

        User(email=email, password=password).save()
        logic.set_session_data(request, "login_token", email)
        messages.success(request, "Logged in successfully")
        return redirect("/dashboard")


def login(request):
    if logic.get_session_data(request, "login_token"):
        return redirect("/dashboard")

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        user = User.objects.filter(email=email).filter(password=password).first()

        if user:
            logic.set_session_data(request, "login_token", email)
            messages.success(request, "Logged in successfully")
            return redirect("/dashboard")
        else:
            messages.error(request, "Inavlid Credentials")
            return redirect("/get_started#login-tab-content")


@logic.auth()
def logout(request):
    logic.delete_session_data(request, "login_token")
    messages.success(request, "Logged out successfully")
    return redirect("/get_started#login-tab-content")
