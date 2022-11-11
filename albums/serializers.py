from rest_framework import serializers
from .models import *
from artists.models import *

class ArtistSerializer(serializers.ModelSerializer):
    class Meta:
        model = Artist
        fields = "__all__"


class AlbumSerializer(serializers.ModelSerializer):
    name = serializers.CharField(default='New Album', max_length=100, required=False)
    artist = ArtistSerializer(many=False,read_only=True)
    cost = serializers.DecimalField(required=True, decimal_places=2, max_digits=10)
    release_datetime = serializers.DateTimeField(required=True)
    propriet = serializers.BooleanField(default=False)
    
    class Meta:
        model = Album
        fields = ('id', 'artist', 'name', 'release_datetime', 'cost', 'propriet')