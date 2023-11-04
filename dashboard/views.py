# Create your views here.

from django.shortcuts import render

from authentication.logic import auth


@auth()
def index(request):
    return render(request, "dashboard/dashboard.html")
