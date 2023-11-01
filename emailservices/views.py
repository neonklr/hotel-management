from django.shortcuts import render
from django.core.mail import send_mail
from django.conf import settings
from datetime import datetime

# Create your views here

def checkin_send_email(request):
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


def checkout_email(request):
    user_email = "ujjwalj12222@gmail.com"

    booking_date_str = "2023-11-05"
    checkout_date_str = str(datetime.today().date())
    perDayPrice = 2000

    booking_date = datetime.strptime(booking_date_str, "%Y-%m-%d")
    checkout_date = datetime.strptime(checkout_date_str, "%Y-%m-%d")

    date_difference = booking_date - checkout_date
    totalDays = date_difference.days

    paidAmount = totalDays * perDayPrice

    customer_name = "Ujjwal Jamuar"

    subject = "Checkout Confirmed"
    message = f"<strong>Dear {customer_name}, <br><br>We hope you have had a pleasant stay with us at Bloom Stays, and we appreciate your choice in selecting our hotel for your accommodation. We are writing to confirm that your check-out has been successfully processed. <br>Here are the details of your check-out: <br><br>Check-Out Date: {checkout_date} <br><br>Total Paid-Amount - {paidAmount} <br><br>Final Bill: Your final bill has been settled with the payment method provided during your check-in, and all charges, including room charges, taxes, and any additional expenses, have been accurately reflected in the bill. <br>We trust that you found your stay comfortable and that our services met your expectations. Your satisfaction is of utmost importance to us, and we are delighted to have had the opportunity to serve you. <br><br>If you have any questions or require a copy of your final invoice, please do not hesitate to reach out to our front desk staff, who will be more than happy to assist you. <br><br>Once again, we thank you for choosing [Hotel Name], and we look forward to welcoming you back in the future. Your feedback and experience with us are invaluable as we continually strive to provide exceptional service to our guests. <br><br>Safe travels, and we hope to see you again soon. <br><br>Warm regards, <br><br>Bloom Stays <br>+91 111 222 0000 </strong>"
    from_email = settings.EMAIL_HOST_USER
    recipient_list = [user_email]

    try:
        send_mail(subject, "", from_email, recipient_list, html_message=message)
        print("email sent")
        message = "Checkout Confirmed."
        return render(request, "Thankyou.html", {"message": message})

    except Exception:
        message = "Something went wrong or Email Address is incorrect!!"
        return render(request, "Error.html", {"message": message})
