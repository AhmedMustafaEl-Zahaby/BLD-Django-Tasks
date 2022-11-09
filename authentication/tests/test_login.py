import pytest 
from rest_framework import status
from ..models import *
from rest_framework.test import APIClient

endpoint1 = '/authentication/login/'
endpoint2 = '/authentication/register/'

def Validate(response , user):
    User = response.data['user']
    assert User['username'] == user['username']
    assert User['email'] == user['email']
    assert User['bio'] == user['bio']
    assert 'token' not in User
    assert 'token' in response.data
    assert 'id' in User
    assert 'password' not in User

@pytest.mark.django_db
def test_sucess_login():
    user_templete = {
        "username" : "Ahmed El-Zahaby",
        "email" : "ahmedelzahaby8122000@gmail.com",
        "password" : "Korobo500@",
        "confirm_password" : "Korobo500@",
        "bio" : "cggvjehkabjnlvkm"
    }
    client = APIClient()
    response = client.post(f'{endpoint2}' , user_templete)
    assert response.status_code == status.HTTP_201_CREATED

    user_login = {
        "username" : "Ahmed El-Zahaby",
        "password" : "Korobo500@"
    }

    response = client.post(f'{endpoint1}' , user_login)
    assert response.status_code == status.HTTP_200_OK 
    Validate(response , user_templete)

@pytest.mark.django_db

def test_fail_login():
    user_templete = {
        "username" : "Ahmed El-Zahaby",
        "email" : "ahmedelzahaby8122000@gmail.com",
        "password" : "Korobo500@",
        "confirm_password" : "Korobo500@",
        "bio" : "cggvjehkabjnlvkm"
    }
    client = APIClient()
    response = client.post(f'{endpoint1}' , {})
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    response = client.post(f'{endpoint2}' , user_templete)
    assert response.status_code == status.HTTP_201_CREATED

    user_login = {
        "username" : "Ahmed El-Zahaby",
        "password" : "Korobo500@"
    }

    user_login["username"] = 'Ahmed'
    response = client.post(f'{endpoint1}' , user_login)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    user_login["username"] = 'Ahmed El-Zahaby'
    user_login["password"] = 'Krozo500@'
    response = client.post(f'{endpoint1}' , user_login)
    assert response.status_code == status.HTTP_400_BAD_REQUEST




