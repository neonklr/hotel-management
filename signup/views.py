# Create your views here.
from django.shortcuts import render

from users.models import User
from django.contrib.auth import get_user_model


def register(request):
    user = get_user_model()
    objects = User.objects.all()
    if request.method == "POST":
        user_email = request.POST["user_email"]
        user_password = request.POST["user_password"]
        repass = request.POST["repass"]
        # user_password should match repass
        my_object = User.objects.get(email="user_email")
        if my_object:
            print("alreadyexist")
        else:
            new_entry = User(email="user_email", password="user_password")
            new_entry.save()

    # print("HI", objects)
    # for obj in objects:
    #     field1_value = obj.name
    #     field2_value = obj.email
    #     field3_value = obj.password
    # print(f'Field, Field 2:, Field 3:')

    return render(request, "register.html")


# def login(request):
# return render (request,'register.html')
