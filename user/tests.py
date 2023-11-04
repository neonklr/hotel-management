# Create your tests here.

from datetime import datetime

from django.test import Client, TestCase

from .models import User


class TestViewProfilePage(TestCase):
    def setUp(self):
        self.client = Client()

    def test_page_when_not_logged_in(self):
        response = self.client.get("/user/view/", follow=True)

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

        response = self.client.get("/user/view/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test")
        self.assertContains(response, "test@example.com")
        self.assertContains(response, "Update My Profile")

        self.client.get("/auth/logout/")


class TestUpdateProfilePage(TestCase):
    def setUp(self):
        self.client = Client()

    def test_page_when_not_logged_in(self):
        response = self.client.get("/user/update/", follow=True)

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

        response = self.client.get("/user/update/")
        self.assertEqual(response.status_code, 200)
        self.assertContains(response, "test")
        self.assertContains(response, "test@example.com")
        self.assertContains(response, "Update Profile")

        self.client.get("/auth/logout/")


class TestUserModel(TestCase):
    def setUp(self):
        User.objects.create(
            name="test",
            email="test@example.com",
            password="password",
            address="address",
            phone_number=123,
            date_of_birth=datetime.now(),
        )

    def test_user_model_exists(self):
        user = User.objects.get(name="test")
        self.assertEqual(user.email, "test@example.com")

    def test_user_model_not_exists(self):
        user = User.objects.filter(name="testing")
        self.assertEqual(len(user), 0)
