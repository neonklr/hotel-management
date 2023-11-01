# Create your views here.
from django.shortcuts import render


def new_reservation_view(request):
    return render(request, "new.html")

def update_reservation_view(request):
    return render(request, "update.html")