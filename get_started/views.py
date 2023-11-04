# Create your views here.

from django.shortcuts import render


def index(request):
    return render(request, "get_started/login.html")
