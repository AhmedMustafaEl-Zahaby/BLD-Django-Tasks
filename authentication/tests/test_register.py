from rest_framework import status 
from rest_framework.test import APIClient
import pytest

endpoint = '/authentication/register/'

@pytest.mark.django_db
def test_sucess_register():
    user_templete = {
        "username" : "Ahmed El-Zahaby",
        "email" : "ahmedelzahaby8122000@gmail.com",
        "password" : "Korobo500@",
        "confirm_password" : "Korobo500@",
        "bio" : "cggvjehkabjnlvkm"
    }
    client = APIClient()
    response = client.post(f'{endpoint}', user_templete)
    assert response.status_code == status.HTTP_201_CREATED

@pytest.mark.django_db
def test_fail_register():
    user_templete = {
        "username" : "Ahmed El-Zahaby",
        "email" : "ahmedelzahaby8122000@gmail.com",
        "password" : "Korobo500@",
        "confirm_password" : "Korobo500@",
        "bio" : "cggvjehkabjnlvkm"
    }
    client = APIClient()
    response = client.post(f'{endpoint}', {})
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    response = client.post(f'{endpoint}', user_templete)
    response = client.post(f'{endpoint}', user_templete)
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    user_templete["password"] = user_templete["confirm_password"] = "Krobo"
    response = client.post(f'{endpoint}', user_templete)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    user_templete['password'] = user_templete["confirm_password"] = "Krobo500"
    response = client.post(f'{endpoint}', user_templete)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    user_templete['password'] = user_templete["confirm_password"] = "KroboKramix"
    response = client.post(f'{endpoint}', user_templete)
    assert response.status_code == status.HTTP_400_BAD_REQUEST
    
    user_templete['password'] = user_templete["confirm_password"] = "Krobo500@"
    user_templete['email'] = "Ahmedelzahaby8120"
    response = client.post(f'{endpoint}', user_templete)
    assert response.status_code == status.HTTP_400_BAD_REQUEST