from django_filters import rest_framework
from albums.models import *

class AlbumFilter(rest_framework.FilterSet):

    class Meta:
        model = Album
        fields = {
            'cost' : ['gte', 'lte'],
            'name' : ['icontains']
        }