# Create your tests here.

from datetime import datetime

from django.test import Client, TestCase

from user.models import User

from .models import Room


class TestViewReservationPage(TestCase):
    def setUp(self):
        self.client = Client()

    def test_page_when_not_logged_in(self):
        response = self.client.get("/reservation/view/", follow=True)

        response = self.assertRedirects(
            response, "/get_started/", status_code=302, target_status_code=200, fetch_redirect_response=True
        )

    def test_page_when_logged_in(self):
        User.objects.create(
            name="test",
            email="test@example.com",
            password="password",
            address="address",
            phone_number=123,
            date_of_birth=datetime.now(),
        )

        self.client.post("/auth/login/", {"email": "test@example.com", "password": "password"}, follow=True)

        response = self.client.get("/reservation/view/")
        self.assertEqual(response.status_code, 200)

        self.client.get("/auth/logout/")


class TestNewReservationPage(TestCase):
    def setUp(self):
        self.client = Client()

    def test_page_when_not_logged_in(self):
        response = self.client.get("/reservation/new/", follow=True)

        response = self.assertRedirects(
            response, "/get_started/", status_code=302, target_status_code=200, fetch_redirect_response=True
        )

    def test_page_when_logged_in(self):
        User.objects.create(
            name="test",
            email="test@example.com",
            password="password",
            address="address",
            phone_number=123,
            date_of_birth=datetime.now(),
        )

        self.client.post("/auth/login/", {"email": "test@example.com", "password": "password"}, follow=True)

        response = self.client.get("/reservation/new/")
        self.assertEqual(response.status_code, 200)

        self.client.get("/auth/logout/")


class TestNewReservation(TestCase):
    def setUp(self):
        Room.objects.create(type="Delux", no=1, price=100)

        User.objects.create(
            name="test",
            email="test@example.com",
            password="password",
            address="address",
            phone_number=123,
            date_of_birth=datetime.now(),
        )

        self.client = Client()

    def test_new_reservation(self):
        self.client.post("/auth/login/", {"email": "test@example.com", "password": "password"}, follow=True)

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
        self.assertContains(response, "Delux")

        self.client.get("/auth/logout/")
