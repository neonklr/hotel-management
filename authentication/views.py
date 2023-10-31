# Create your views here.

from django.shortcuts import redirect
from django.contrib import messages
from django.contrib.auth.models import User



from users.models import User

def signup(request):
    if request.method == 'POST':
        email = request.POST.get('user_email')
        password = request.POST.get('user_password')
        repass = request.POST.get('repass')

        if not password == repass:
            messages.error(request,'Password does not match re-entered password')
            return redirect("/get_started#signup-tab-content")

        if User.objects.filter(email=email).exists():
            messages.error(request,'You are already registered... please login again')
            return redirect("/get_started#login-tab-content")
        

        User(email=email, password=password).save()

        return redirect("/dashboard")



def login(request):
    if request.method == 'POST':
        email = request.POST['email']
        password = request.POST['password']

        user = User.objects.get(email=email)

        if user and (user.password == password):
            messages.success(request,'Logged in successfully')
            return redirect("/dashboard")
        else:
           messages.error(request,'Inavlid Credentials')
           return redirect("/get_started#login-tab-content")

