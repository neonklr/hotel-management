# Create your tests here.

from django.test import Client, TestCase


class TestHomePage(TestCase):
    def setUp(self):
        self.client = Client()

    def test_index_page(self):
        response = self.client.get("/")

        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, "home/index.html")

        self.assertContains(response, "Get Started")
        self.assertContains(response, "BLOOM ❄ STAYS")
