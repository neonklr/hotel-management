from django.shortcuts import render
from django.core.mail import send_mail, EmailMessage
from django.conf import settings
from datetime import datetime
from reportlab.lib.pagesizes import letter
from reportlab.platypus import SimpleDocTemplate, Paragraph, Spacer, Table, TableStyle
from reportlab.lib.styles import getSampleStyleSheet, ParagraphStyle
from reportlab.lib import colors
from reportlab.lib.units import inch
import os

# Create your views here

def generate_invoice(customer_name, room_type, price, days):
    current_directory = os.getcwd() + '/emailservices/'

    # Define the PDF filename and path
    pdf_filename = os.path.join(current_directory, "invoice.pdf")

    # Create a PDF document
    doc = SimpleDocTemplate(pdf_filename, pagesize=letter)
    elements = []

    # Define the stylesheet
    styles = getSampleStyleSheet()
    styles['Normal'].fontName = 'SourceSansPro'
    styles['Normal'].fontSize = 11
    
    styles.add(ParagraphStyle(name='Salutation',  fontSize=40, spaceAfter=12))
    styles.add(ParagraphStyle(name='Address',  fontSize=11, leading=14))
    styles.add(ParagraphStyle(name='TableHeader',  fontSize=10, alignment=1, textColor=colors.HexColor('#a9a')))
    styles.add(ParagraphStyle(name='TableValue',  fontSize=11, alignment=1, leading=14))

    # Title
    elements.append(Paragraph("Bloom ❄️ Stays", styles['Title']))
    elements.append(Spacer(1, 12))

    
    elements.append(Spacer(1, 24))

    # Informations
    information_data = [
        ('Customer Name',customer_name),
        ("Invoice number", "12345"),
        ("Date", str(datetime.today().date())),
        ("Time", str(datetime.now().strftime('%H:%M')))
    ]
    information_table = Table(information_data, colWidths=[1 * inch, 2 * inch])
    information_table.setStyle(TableStyle([
        # ('FONTNAME', (0, 0), (-1, -1), 'SourceSansPro'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('ALIGN', (0, 0), (0, -1), 'LEFT'),
        ('ALIGN', (1, 0), (1, -1), 'RIGHT'),
    ]))
    elements.append(information_table)
    elements.append(Spacer(1, 72))

    # Items
    item_data = [
        ["Description", "Price", "Days", "Subtotal"],
        [room_type, price, days, price*days],
    ]
    item_table = Table(item_data, colWidths=[4.5 * inch, 1 * inch, 1 * inch, 1.5 * inch])
    item_table.setStyle(TableStyle([
        # ('FONTNAME', (0, 0), (-1, -1), 'SourceSansPro'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f6f6f6')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#a9a')),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (0, 0), (-1, 0), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black)
    ]))
    elements.append(item_table)
    elements.append(Spacer(1, 60))

    # Total
    total_data = [
        ["Paid On", "Paid by", "Total Amount"],
        [str(datetime.today().date()), customer_name, price*days]
    ]
    total_table = Table(total_data, colWidths=[2 * inch, 2 * inch, 2 * inch])
    total_table.setStyle(TableStyle([
        # ('FONTNAME', (0, 0), (-1, -1), 'SourceSansPro'),
        ('FONTSIZE', (0, 0), (-1, -1), 11),
        ('BACKGROUND', (0, 0), (-1, 0), colors.HexColor('#f6f6f6')),
        ('TEXTCOLOR', (0, 0), (-1, 0), colors.HexColor('#a9a')),
        ('ALIGN', (0, 0), (-1, -1), 'CENTER'),
        ('ALIGN', (0, 0), (-1, 0), 'LEFT'),
        ('ALIGN', (1, 0), (-1, -1), 'LEFT'),
        ('ALIGN', (2, 0), (-1, -1), 'RIGHT'),
        ('VALIGN', (0, 0), (-1, -1), 'MIDDLE'),
        ('GRID', (0, 0), (-1, -1), 0.5, colors.black)
    ]))
    elements.append(total_table)

    elements.append(Spacer(1, 60))

    thank_you_text = Paragraph("Thank you for choosing Bloom Stays Hotel!", styles['Title'])

    elements.append(thank_you_text)

    doc.build(elements)

def checkin_send_email(request):

    customer_name = 'Ujjwal Jamuar'
    room_type = 'Deluxe'
    price = 2000
    days = 2
    
    subject = "Booking Confirmed"
    message = f"""<strong>Dear {customer_name},<br><br>
                We are delighted to confirm your upcoming check-in at Bloom Stays on {datetime.today().date()}. We look forward to providing you with a comfortable and enjoyable stay. <br><br>
                Here are the details of your reservation: <br><br>
                Check-in Date: {datetime.today().date()} <br>
                Room Type: {room_type} <br>
                Price: {price} <br>
                Number of Days: {days} <br><br>

                Please note the following: <br><br>

                Check-in Time: {str(datetime.now().strftime('%H:%M'))} <br><br>

                Upon arrival, our friendly front desk staff will be available to assist you with a smooth check-in process. If you have any specific preferences or need further assistance, please do not hesitate to let us know in advance or at the front desk. <br><br>

                We hope you have a pleasant and memorable stay with us. Should you have any questions or require further information, please feel free to contact our guest services. <br><br>

                Thank you for choosing Bloom Stays, and we look forward to providing you with exceptional service during your stay. <br><br>

                Safe travels, and we'll see you soon! <br><br>
                Warm regards,<br>
                Prithvi Raj Chauhan<br>
                Email Services Department<br>
                Bloom Stays<br>+91 111 222 0000
                </strong>
                """
    from_email = settings.EMAIL_HOST_USER
    recipient_list = ["ujjwalj12222@gmail.com"]

    try:
        generate_invoice(customer_name, room_type, price, days)

        # send_mail(subject, message, from_email, recipient_list)
        mail = EmailMessage(subject=subject, body= message, from_email=from_email, to=recipient_list)
        mail.content_subtype = 'html'
        mail.attach_file(f'{settings.BASE_DIR}/emailservices/invoice.pdf')

        mail.send()
        print("email sent")

        message = "Thanks a bunch for booking at our hotel. It means a lot to us, just like you do! "

        return render(request, "Thankyou.html", {"message": message})

    except Exception as e:
        return render(request, "Error.html", {"message": e})

def cancel_res(request):
    return render(request, "EarlyCancelModal.html")


def send_refund_email(request):
    price = 2000
    booking_till_str = "2023-11-05"
    checkout_date_str = str(datetime.today().date())

    booking_till = datetime.strptime(booking_till_str, "%Y-%m-%d")
    checkout_date = datetime.strptime(checkout_date_str, "%Y-%m-%d")

    date_difference = booking_till - checkout_date
    daysleft = date_difference.days
    # paidAmount = ''
    refundAmount = daysleft * price

    customer_name = "Ujjwal Jamuar"

    subject = "Booking Cancelled"
    message = f"""<strong>We wanted to confirm that we have received your request to cancel your reservation with us. 
                We understand that sometimes plans change, and we're here to assist you with this process.<br><br>
                Here are the details of your canceled reservation: <br>Reservation ID: [Reservation ID]<br>Customer Name: {customer_name}<br>
                Reservation Date: {booking_till_str}<br>
                Cancellation Date: {checkout_date_str}<br>
                Refund Amount: {refundAmount}<br><br>
                If you have any questions or require any further assistance regarding your cancellation or potential rebooking, 
                please don't hesitate to contact our customer service team at [Customer Service Email] or [Customer Service Phone Number]. 
                We're here to help and ensure your experience with us is as smooth as possible.Thank you for considering our services, 
                and we hope to have the opportunity to serve you in the future. We value your business and appreciate your understanding.<br><br>
                Warm regards,<br>
                Prithvi Raj Chauhan<br>
                Email Services Department<br>
                Bloom Stays<br>+91 111 222 0000
                """

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
    price = 2000

    booking_date = datetime.strptime(booking_date_str, "%Y-%m-%d")
    checkout_date = datetime.strptime(checkout_date_str, "%Y-%m-%d")

    date_difference = booking_date - checkout_date
    totalDays = date_difference.days

    paidAmount = totalDays * price

    customer_name = "Ujjwal Jamuar"

    subject = "Checkout Confirmed"
    message = f"""<strong>Dear {customer_name}, <br><br>
                We hope you have had a pleasant stay with us at Bloom Stays, and we appreciate your choice in selecting our hotel for your accommodation. 
                We are writing to confirm that your check-out has been successfully processed. <br>
                Here are the details of your check-out: <br><br>
                Check-Out Date: {checkout_date} <br><br>
                Total Paid-Amount - {paidAmount} <br><br>
                Final Bill: Your final bill has been settled with the payment method provided during your check-in, and all charges, including room charges, taxes, and any additional expenses, have been accurately reflected in the bill. <br>
                We trust that you found your stay comfortable and that our services met your expectations. 
                Your satisfaction is of utmost importance to us, and we are delighted to have had the opportunity to serve you. <br><br>
                If you have any questions or require a copy of your final invoice, please do not hesitate to reach out to our front desk staff, who will be more than happy to assist you. <br><br>
                Once again, we thank you for choosing Bloom Stays, and we look forward to welcoming you back in the future. 
                Your feedback and experience with us are invaluable as we continually strive to provide exceptional service to our guests. <br><br>
                Safe travels, and we hope to see you again soon. <br><br>
                Warm regards, <br><br>
                Bloom Stays <br>
                +91 111 222 0000 
                </strong>
                """
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
