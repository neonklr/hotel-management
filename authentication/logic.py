from django.contrib import messages
from django.shortcuts import redirect

from users.models import User


# storing the data
def set_session_data(request, key, value):
    request.session[key] = value


# retreiving the data
def get_session_data(request, key):
    return request.session[key]


# deleting the data
def delete_session_data(request, key):
    return request.session.pop(key, None)


def profile_is_empty(user):
    return not bool(
        user.name and user.email and user.password and user.phone_number and user.address and user.date_of_birth
    )


def auth(path):
    def outer_function(func):
        def inner_function(request, *args, **kwargs):
            user = None

            if email := request.session.get("login_token", None):
                user = User.objects.get(email=email)

            if not user:
                messages.error(request, "Please login to continue...")
                return redirect("/get_started#login-tab-content")

            if path == "/user/update":
                return func(request, *args, user=user, **kwargs)

            if profile_is_empty(user):
                return redirect("/user/update")

            return func(request, *args, user=user, **kwargs)

        return inner_function

    return outer_function
