# Create your views here.
from django.shortcuts import render
from django.http import HttpRequest

from users.models import User

def login(request):
    return render (request,'login.html')
