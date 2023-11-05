# Create your tests here.

from datetime import datetime

from django.test import Client, TestCase

from helper.tests import login_user

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
        with login_user(self.client):
            response = self.client.get("/user/view/")
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "test")
            self.assertContains(response, "test@example.com")
            self.assertContains(response, "Update My Profile")
            self.assertTemplateUsed(response, "user/view.html")


class TestUpdateProfilePage(TestCase):
    def setUp(self):
        self.client = Client()

    def test_page_when_not_logged_in(self):
        response = self.client.get("/user/update/", follow=True)

        response = self.assertRedirects(
            response, "/get_started/", status_code=302, target_status_code=200, fetch_redirect_response=True
        )

    def test_page_when_logged_in(self):
        with login_user(self.client):
            response = self.client.get("/user/update/")
            self.assertEqual(response.status_code, 200)
            self.assertContains(response, "test")
            self.assertContains(response, "test@example.com")
            self.assertContains(response, "Update Profile")
            self.assertTemplateUsed(response, "user/update.html")


class TestUserModel(TestCase):
    def setUp(self):
        User.objects.create(
            name="testing",
            email="testing@example.com",
            password="password",
            address="address",
            phone_number=123,
            date_of_birth=datetime.now(),
        )

    def test_user_model_exists(self):
        user = User.objects.get(name="testing")
        self.assertEqual(user.email, "testing@example.com")

    def test_user_model_not_exists(self):
        user = User.objects.filter(name="testx")
        self.assertEqual(len(user), 0)
