from django.urls import path
from . import views

urlpatterns = [
    path('setlogin/', views.set_session_data, name='set_session_data'), # type: ignore
    path('checklogin/', views.get_session_data, name='get_session_data'), #type:ignore
    path('outlogin/', views.logout_view, name='logout'), #type:ignore
]