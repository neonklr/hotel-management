from django.http import HttpResponse
from django.contrib.auth import logout


# storing the data
def set_session_data(request):
    request.session["user_id"] = 123
    return HttpResponse("session added")


# retreiving the data
def get_session_data(request):
    # user_id = request.session.get('hotel_management', None)
    user_id = request.COOKIES["hotel_management"]
    if user_id is not None:
        # Do something with the user ID/ Fetching data from login
        print(user_id)
    else:
        # User not logged in or session expired
        pass
    return HttpResponse(user_id)


# logout session
def logout_view(request):
    logout(request)
    return HttpResponse("User Logged out")
