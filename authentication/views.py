# Create your views here.

from django.contrib import messages
from django.shortcuts import redirect

from users.models import User

from . import logic

import hashlib
import os


# Function to hash passwords using SHA-256
def hash_password(password, salt=None):
    if salt is None:
        salt = os.urandom(16)  # Generate a random salt if not provided

    # Hash the password using SHA-256 and the salt
    hasher = hashlib.sha256()
    hasher.update(salt)
    hasher.update(password.encode("utf-8"))
    hashed_password = hasher.digest()

    # Return the salt and hashed password
    return hashed_password


# Function to hash passwords using SHA-256
def hashpassword(password, salt=None):
    if salt is None:
        salt = os.urandom(16)  # Generate a random salt if not provided

    # Hash the password using SHA-256 and the salt
    hasher = hashlib.sha256()
    hasher.update(salt)
    hasher.update(password.encode("utf-8"))
    hashed_password = hasher.digest()

    # Return the salt and hashed password
    return hashed_password, salt


# Function to verify passwords
def verify_password(entered_password, stored_salt, stored_hashed_password):
    # Verify the entered password using the stored salt and hashed password
    hasher = hashlib.sha256()
    hasher.update(stored_salt)
    hasher.update(entered_password.encode("utf-8"))
    hashed_password = hasher.digest()

    # Compare the computed hash with the stored hash
    return hashed_password == stored_hashed_password


# Example usage
# plain_password = "user_input_password"

# Hash the password and get the salt and hashed password
# salt, hashed_password = hash_password(plain_password)

# Store the salt and hashed_password in your database
# ...

# Later during authentication, verify the entered password
# entered_password = "user_input_password"
# if verify_password(entered_password, salt, hashed_password):
#     print("Authentication successful")
# else:
#     print("Authentication failed")


def signup(request):
    if logic.get_session_data(request, "login_token"):
        return redirect("/dashboard")

    if request.method == "POST":
        email = request.POST.get("user_email")
        password = request.POST.get("user_password")
        repass = request.POST.get("repass")

        if not password == repass:
            messages.error(request, "Password does not match re-entered password")
            return redirect("/get_started#signup-tab-content")

        if User.objects.filter(email=email).exists():
            messages.error(request, "You are already registered... please login again")
            return redirect("/get_started#login-tab-content")

        # hashed_password = bcrypt.hashpw(password.encode('utf-8'), bcrypt.gensalt())
        # print(hashed_password,"pass")

        print(hash_password(password), "pass")
        User(email=email, password=hash_password(password)).save()
        logic.set_session_data(request, "login_token", email)
        messages.success(request, "Logged in successfully")
        return redirect("/dashboard")


def login(request):
    if logic.get_session_data(request, "login_token"):
        return redirect("/dashboard")

    if request.method == "POST":
        email = request.POST["email"]
        password = request.POST["password"]

        # user = User.objects.filter(email=email).filter(password=password).first()
        user = User.objects.get(email=email)

        stored_hashed_password = user.password
        hashpass, salt = hashpassword(password)
        if user and verify_password(password, salt, hashpass):
            # bcrypt.checkpw(password.encode('utf-8'), stored_hashed_password.encode('utf-8')):
            # if bcrypt.checkpw(entered_password.encode('utf-8'), stored_hashed_password):

            # if user.email and bcrypt.checkpw(password.encode('utf8'), user.password):
            # if user:
            logic.set_session_data(request, "login_token", email)
            messages.success(request, "Logged in successfully")
            return redirect("/dashboard")
        else:
            messages.error(request, "Inavlid Credentials")
            return redirect("/get_started#login-tab-content")


@logic.auth()
def logout(request):
    logic.delete_session_data(request, "login_token")
    messages.success(request, "Logged out successfully")
    return redirect("/get_started#login-tab-content")
