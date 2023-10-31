# Create your views here.
from django.shortcuts import render, HttpResponse

def update_profile(request, user=None):
    if user:
        return render(request, "update.html", {"user": user})
    
    return HttpResponse("<h3>direct access forbidden</h3>")


def view_profile(request, user=None):
    if user:
        return render(request, "view.html", {"user": user})
    
    return HttpResponse("<h3>direct access forbidden</h3>")