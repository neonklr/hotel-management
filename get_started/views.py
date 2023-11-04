# Create your views here.

from django.shortcuts import redirect, render

from authentication.logic import get_session_data


def index(request):
    if get_session_data(request, "login_token"):
        return redirect("/dashboard/")

    return render(request, "get_started/index.html")
