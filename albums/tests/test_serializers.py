from users.models import *
from artists.models import *
from ..models import *
from ..serializers import *
from datetime import datetime
from dateutil.parser import parse
from decimal import Decimal
import zoneinfo, pytest

@pytest.mark.django_db
def test_valid_data():
    temp = {
        "name" : "Kamakazi",
        "release_datetime" : datetime(2026, 12, 8, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
        "cost" : 1600,
        "propriet" : True
    }
    serializer = AlbumSerializer(data=temp)
    serializer.is_valid(raise_exception=False)
    assert not serializer.errors
    
    assert temp["name"] == "Kamakazi"
    assert temp["release_datetime"] == datetime(2026, 12, 8, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')) 
    assert temp["cost"] == 1600
    assert temp["propriet"] == True

@pytest.mark.django_db
def test_missing_data():
    temp = {
        "name" : "Kamakazi",
        "release_datetime" : datetime(2026, 12, 8, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC'))
    }
    serializer = AlbumSerializer(data=temp)
    serializer.is_valid(raise_exception=False)
    assert serializer.errors
    assert serializer.errors.keys() == set(['cost'])

    temp = {
        "name" : "Kamakazi",
        "cost": 1600
    }
    serializer = AlbumSerializer(data=temp)
    serializer.is_valid(raise_exception=False)
    assert serializer.errors
    assert serializer.errors.keys() == set(['release_datetime'])

    temp = {
        "release_datetime" : datetime(2026, 12, 8, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
        "cost": 1600
    }
    serializer = AlbumSerializer(data=temp)
    serializer.is_valid(raise_exception=False)
    assert not serializer.errors

@pytest.mark.django_db

def test_unvalid_data():
        temp = {
        "name" : "Kamakazi",
        "release_datetime" : datetime(2026, 12, 8, 0, 0, tzinfo=zoneinfo.ZoneInfo(key='UTC')),
        "cost" : "ahmed",
        "propriet" : True
        }
        serializer = AlbumSerializer(data=temp)
        serializer.is_valid(raise_exception=False)
        assert serializer.errors
        assert serializer.errors.keys() == set(['cost'])


