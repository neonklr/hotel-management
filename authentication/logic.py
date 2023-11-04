import hashlib

from django.contrib import messages
from django.shortcuts import redirect

from user.models import User


# storing the data
def set_session_data(request, key, value):
    request.session[key] = value


# retreiving the data
def get_session_data(request, key):
    return request.session.get(key, False)


# deleting the data
def delete_session_data(request, key):
    return request.session.pop(key, None)


def profile_is_empty(user):
    return not bool(
        user.name and user.email and user.password and user.phone_number and user.address and user.date_of_birth
    )


def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()


def auth(by_pass_route=False):
    def outer_function(func):
        def inner_function(request, *args, **kwargs):
            user = None

            if email := request.session.get("login_token", None):
                user = User.objects.get(email=email)

            if not user:
                messages.error(request, "Please login to continue...")
                return redirect("/get_started#login-tab-content")

            request.user = user

            if by_pass_route:
                return func(request, *args, **kwargs)

            if profile_is_empty(user):
                return redirect("/user/update")

            return func(request, *args, **kwargs)

        return inner_function

    return outer_function
