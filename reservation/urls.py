"""
URL configuration for hotel_management project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path

from . import views

urlpatterns = [
    path("new/", views.new_reservation, name="new_reservation"),
    path("history/", views.previous_reservation, name="previous_reservation"),
    path("cancel/<str:uuid>/", views.cancel_reservation, name="cancel_reservation"),
    # path("checkout/<str:uuid>/", views.checkout_room, name="checkout_room"),
    path("book_room/", views.book_room),
]
