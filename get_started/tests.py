# Create your tests here.


from django.test import Client, TestCase

from helper.tests import login_user


class TestGetStartedPage(TestCase):
    def setUp(self):
        self.client = Client()
        self.client.session.pop("login_token", None)

    def test_page_when_not_logged_in(self):
        response = self.client.get("/get_started/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "get_started/index.html")

        self.assertContains(response, "Login")
        self.assertContains(response, "SignUp")

    def test_page_when_signed_up(self):
        self.client.post(
            "/auth/signup/",
            {"user_email": "test@example.com", "user_password": "test1234", "repass": "test1234"},
            follow=True,
        )

        response = self.client.get("/get_started/", follow=True)

        self.assertRedirects(
            response, "/user/update/", status_code=302, target_status_code=200, fetch_redirect_response=True
        )
        self.client.get("/auth/logout/")

    def test_page_when_logged_in(self):
        with login_user(self.client):
            response = self.client.get("/get_started/", follow=True)

            self.assertRedirects(
                response, "/dashboard/", status_code=302, target_status_code=200, fetch_redirect_response=True
            )

            self.assertTemplateUsed(response, "dashboard/dashboard.html")
