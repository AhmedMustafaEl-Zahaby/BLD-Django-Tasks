from rest_framework import serializers
from .models import *
from artists.models import *


class AlbumSerializer(serializers.ModelSerializer):

    name = serializers.CharField(default='New Album', max_length=100, required=False)
    artist = serializers.SerializerMethodField('Artist_data')
    cost = serializers.DecimalField(required=True, decimal_places=2, max_digits=10)
    release_datetime = serializers.DateTimeField(required=True)
    propriet = serializers.BooleanField(default=False)
    
    class Meta:
        model = Album
        fields = ('id', 'artist', 'name', 'release_datetime', 'cost', 'propriet')    

    def Artist_data(self, obj):
        return {
            "id": obj.artist.id,
            "Stage_name": obj.artist.Stage_name,
            "Social_link": obj.artist.Social_link
        }