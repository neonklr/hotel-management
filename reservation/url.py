from django.urls import path
from . import views

urlpatterns = [
    path("check_availability/", views.check_availability, name="check_availability"),  # type:ignore
]
