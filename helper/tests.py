from contextlib import contextmanager
from datetime import datetime

from authentication.logic import hash_password
from user.models import User


@contextmanager
def login_user(client):
    user = User.objects.create(
        name="test",
        email="test@example.com",
        password=hash_password("password"),
        address="address",
        phone_number=123,
        date_of_birth=datetime.now(),
    )

    client.post("/auth/login/", {"email": "test@example.com", "password": "password"}, follow=True)

    yield user

    client.get("/auth/logout/")
