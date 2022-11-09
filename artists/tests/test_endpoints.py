import pytest 
from rest_framework import status
from ..models import *
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_sucess_retrieve():
    endpoint = '/artist/'
    templete = {
        "Stage_name" : "ahmedMustag",
        "Social_link" : "https://www.youtube.com/watch?v=LYX6nlECcro"
    }
    client = APIClient()
    # first create artist 

    response = client.post(f'{endpoint}', templete)
    assert response.status_code == status.HTTP_201_CREATED

    #then we retrieve it 

    response = client.get(f'{endpoint}1')
    assert response.status_code == status.HTTP_200_OK


@pytest.mark.django_db
def  test_fail_retrieve(client):

    response = client.get('/artist/1')
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_sucess_creation():
    client = APIClient()
    endpoint = "/artist/"
    templete = {
        "Stage_name" : "ahmedMustag",
        "Social_link" : "https://www.youtube.com/watch?v=LYX6nlECcro"
    }
    response = client.post(f'{endpoint}', templete)
    assert response.status_code == status.HTTP_201_CREATED


@pytest.mark.django_db
def test_create_failed():

    endpoint = '/artist/'
    templete = {
        "Stage_name" : "Ahmed El-Zahaby",
        "Social_link" : "www.facebook.com/123"
    }
    client = APIClient()
    response = client.post(f'{endpoint}', {})
    assert response.status_code == status.HTTP_400_BAD_REQUEST

    response = client.post(f'{endpoint}', templete)
    assert response.status_code == status.HTTP_400_BAD_REQUEST


@pytest.mark.django_db
def test_sucess_update():
    endpoint = '/artist/'
    templete = {
        "Stage_name" : "ahmedMustag",
        "Social_link" : "https://www.youtube.com/watch?v=LYX6nlECcro"
    }
    client = APIClient()

    response = client.post(f'{endpoint}', templete)
    assert response.status_code == status.HTTP_201_CREATED

    templete["Stage_name"] = "Ahmed"
    response = client.put(f'{endpoint}1', templete , kwargs={'pk': 1})
    assert response.status_code == status.HTTP_200_OK

    assert response.data["Stage_name"] == "Ahmed"


@pytest.mark.django_db
def test_fail_update():    
    endpoint = '/artist/'
    templete = {
        "Stage_name" : "ahmedMustag",
        "Social_link" : "https://www.youtube.com/watch?v=LYX6nlECcro"
    }
    client = APIClient()

    response = client.put(f'{endpoint}1', templete, kwargs={'pk': 1})
    assert response.status_code == status.HTTP_404_NOT_FOUND
    
    response = client.post(f'{endpoint}', templete)
    assert response.status_code == status.HTTP_201_CREATED

    templete["Stage_name"] = "Ahmed"
    response = client.put(f'{endpoint}/2', templete)
    assert response.status_code == status.HTTP_404_NOT_FOUND


@pytest.mark.django_db
def test_sucess_delete():

    endpoint = '/artist/'
    templete = {
        "Stage_name" : "ahmedMustag",
        "Social_link" : "https://www.youtube.com/watch?v=LYX6nlECcro"
    }
    
    client = APIClient()

    response = client.post(f'{endpoint}', templete)
    assert response.status_code == status.HTTP_201_CREATED
    
    response = client.delete(f'{endpoint}1')
    assert response.status_code == status.HTTP_200_OK

    response = client.get(f'{endpoint}1')
    assert response.status_code == status.HTTP_404_NOT_FOUND

def test_fail_delete():
    endpoint = '/artist/'
    client = APIClient()
    response = client.delete(f'{endpoint}/1')
    assert response.status_code == status.HTTP_404_NOT_FOUND