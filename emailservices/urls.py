from django.urls import path
from . import views

urlpatterns = [
    path("checkin/", views.checkin_send_email, name="checkin_send_email"),
    path("earlycancel/", views.cancel_res, name="cancel_refund_modal"),
    path("earlycancel/cancel/", views.send_refund_email, name="cancel_refund_mail"),
    path("checkout/", views.checkout_email, name="checkout_email"),

]
