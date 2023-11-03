# Create your views here.

from django.shortcuts import render
from authentication.logic import auth
from users.models import User
from authentication.logic import get_session_data

#def profilename(request):
   
       # user = User.objects.get(email=email)

@auth()
def index(request):
    user=get_session_data(request, "login_token")
    split_value=user.split("@")
    firstname=split_value[0]
    print(firstname,"user")
    # d={
    #     firstname
    # }
    return render(request, "dashboard/dashboard.html", {'name':firstname} )