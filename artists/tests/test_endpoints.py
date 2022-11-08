import pytest 
from rest_framework import status
from ..models import *
from rest_framework.test import APIClient


@pytest.mark.django_db
def test_sucess_creation():
    client = APIClient()
    endpoint = "/artist/"
    templete = {
        "Stage_name" : "Ahmed El-Zahaby",
        "Social_link" : "www.facebook.com/123"
    }
    response = client.post(f'{endpoint}', templete)
    assert response.status_code == status.HTTP_201_CREATED