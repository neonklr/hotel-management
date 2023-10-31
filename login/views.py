# Create your views here.
from django.shortcuts import render


def login(request):
    return render(request, "login.html")
