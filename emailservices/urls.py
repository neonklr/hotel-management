from django.urls import path

from . import views

urlpatterns = [
    path("checkin/<str:uuid>/", views.checkin_send_email, name="checkin_send_email"),
    path("earlycancel/<str:uuid>/", views.send_refund_email, name="cancel_refund_mail"),
    path("checkout/<str:uuid>/", views.checkout_email, name="checkout_email"),
]
