from django.shortcuts import render, redirect
from django.core.mail import send_mail
from django.http import HttpResponse
from django.conf import settings

# Create your views here.

def home(request):
    return render(request, 'index.html')


def send_email(request):
    subject = 'Booking Details'
    message = f'Thank You for booking at our hotel. \nYour total paid amount is ---'
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ['ujjwalj12222@gmail.com']

    send_mail(subject, message, from_email, recipient_list)

    return render(request, 'Thankyou.html')