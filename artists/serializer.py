from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError 

class ArtistSerializer(serializers.ModelSerializer):
	class Meta:
		model = Artist
		fields = "__all__"