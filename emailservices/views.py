from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime

# Create your views here


def send_email(request):
    subject = "Booking Confirmed"
    message = "Thank You for booking at our hotel. \nYour total paid amount is ---"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["ujjwalj12222@gmail.com"]

    try:
        send_mail(subject, message, from_email, recipient_list)
        print("email sent")

        message = "Thanks a bunch for booking at our hotel. It means a lot to us, just like you do! "

        return render(request, "Thankyou.html", {"message": message})

    except Exception:
        message = "Wrong Email Address!!"
        return render(request, "Error.html", {"message": message})


def cancel_res(request):
    return render(request, "EarlyCancelModal.html")


def send_refund_email(request):
    perDayPrice = 2000
    booking_till_str = "2023-11-05"
    checkout_date_str = str(datetime.today().date())

    booking_till = datetime.strptime(booking_till_str, "%Y-%m-%d")
    checkout_date = datetime.strptime(checkout_date_str, "%Y-%m-%d")

    date_difference = booking_till - checkout_date
    daysleft = date_difference.days
    # paidAmount = ''
    refundAmount = daysleft * perDayPrice

    customer_name = "Ujjwal Jamuar"

    subject = "Booking Cancelled"
    message = f"<strong>We wanted to confirm that we have received your request to cancel your reservation with us. We understand that sometimes plans change, and we're here to assist you with this process.<br><br>Here are the details of your canceled reservation: <br>Reservation ID: [Reservation ID]<br>Customer Name: {customer_name}<br>Reservation Date: {booking_till_str}<br>Cancellation Date: {checkout_date_str}<br>Refund Amount: {refundAmount}<br><br>If you have any questions or require any further assistance regarding your cancellation or potential rebooking, please don't hesitate to contact our customer service team at [Customer Service Email] or [Customer Service Phone Number]. We're here to help and ensure your experience with us is as smooth as possible.Thank you for considering our services, and we hope to have the opportunity to serve you in the future. We value your business and appreciate your understanding.<br><br>Warm regards,<br>Prithvi Raj Chauhan<br>Email Services Department<br>Bloom Stays<br>+91 111 222 0000"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["ujjwalj12222@gmail.com"]

    try:
        send_mail(subject, "", from_email, recipient_list, html_message=message)
        print("email sent")
        message = "Your reservation has been cancelled."
        return render(request, "Thankyou.html", {"message": message})

    except Exception:
        message = "Wrong Email Address!!"
        return render(request, "Error.html", {"message": message})