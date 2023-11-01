from django.urls import path
from . import views

urlpatterns = [
    path("send_email/", views.send_email, name="send_email"),
    path("earlycancel/", views.cancel_res, name="cancel_refund_modal"),
    path("earlycancel/cancel/", views.send_refund_email, name="cancel_refund_mail"),
    path("checkout/", views.checkout_email, name="checkout_email"),
]
