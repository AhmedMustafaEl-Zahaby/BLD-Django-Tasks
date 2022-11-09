from rest_framework import status
from rest_framework.test import APIClient
from users.models import User
from knox.auth import AuthToken
import pytest

endpoint = '/authentication/logout/'

@pytest.fixture(autouse=True)
def auth_client(user = None):
    def Auth_client(user = None):
        if user == None:
            user = User.objects.create_user(username="NONE", email="NONE", password="NONE!1")
        _, token = AuthToken.objects.create(user)
        client = APIClient()
        client.credentials(HTTP_AUTHORIZATION='Token ' + token)
        return client

    return Auth_client


@pytest.mark.django_db
def test_sucess_logout(auth_client):
    client = auth_client()
    response = client.post(f'{endpoint}')
    assert response.status_code == status.HTTP_204_NO_CONTENT


@pytest.mark.django_db
def test_fail_logout():
    client = APIClient()
    response = client.post(f'{endpoint}')
    assert response.status_code == status.HTTP_401_UNAUTHORIZED