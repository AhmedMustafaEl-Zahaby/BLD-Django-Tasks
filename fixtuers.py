import pytest

from users.models import User
from knox.auth import AuthToken
from rest_framework.test import APIClient

@pytest.fixture
def auth_client(user = None):
    def Auth_client(user = None):
        if user == None:
            user = User.objects.create_user(username="NONE", email="NONE", password="NONE!1")
        _, token = AuthToken.objects.create(user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        return client

    return Auth_client