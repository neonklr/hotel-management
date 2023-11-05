# Create your tests here.


from django.test import Client, TestCase

from helper.tests import login_user
from user.models import User

from .models import Reservation, ReservationStatus, Room


class TestViewReservationPage(TestCase):
    def setUp(self):
        self.client = Client()

    def test_page_when_not_logged_in(self):
        response = self.client.get("/reservation/view/", follow=True)

        response = self.assertRedirects(
            response, "/get_started/", status_code=302, target_status_code=200, fetch_redirect_response=True
        )

        self.assertTemplateUsed(response, "get_started/index.html")

    def test_page_when_logged_in(self):
        with login_user(self.client):
            response = self.client.get("/reservation/view/")
            self.assertEqual(response.status_code, 200)


class TestNewReservationPage(TestCase):
    def setUp(self):
        self.client = Client()

    def test_page_when_not_logged_in(self):
        response = self.client.get("/reservation/new/", follow=True)

        response = self.assertRedirects(
            response, "/get_started/", status_code=302, target_status_code=200, fetch_redirect_response=True
        )

    def test_page_when_logged_in(self):
        with login_user(self.client):
            response = self.client.get("/reservation/new/")
            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "reservation/new.html")


class TestNewReservation(TestCase):
    def setUp(self):
        Room.objects.create(type="Delux", no=1, price=100)

        self.client = Client()

    def test_new_reservation(self):
        with login_user(self.client):
            response = self.client.post(
                "/reservation/new/",
                {
                    "roomType": "Delux",
                    "checkIn": "2024-01-01",
                    "checkOut": "2024-01-02",
                },
                follow=True,
            )

            self.assertEqual(response.status_code, 200)
            self.assertTemplateUsed(response, "reservation/new.html")
            self.assertContains(response, "Delux")


class TestReservationModel(TestCase):
    def setUp(self) -> None:
        self.room = Room.objects.create(type="Delux", no=1, price=100)
        self.guest = User.objects.create(email="test@example.com", password="test")
        Reservation.objects.create(
            guest=User.objects.get(email="test@example.com"),
            room=Room.objects.get(no=1),
            booked_from="2024-01-01",
            booked_to="2024-01-02",
            payment_method="Cash",
            payment_amount=100,
            booked_on="2024-01-01",
        )

    def test_object_exists(self):
        self.assertTrue(Reservation.objects.exists())

    def test_cancel(self):
        reservation = Reservation.objects.get(guest=self.guest)

        reservation.cancel()

        self.assertEqual(reservation.status, ReservationStatus.cancelled_refund_pending)
