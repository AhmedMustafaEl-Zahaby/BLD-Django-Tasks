from rest_framework import serializers
from .models import *
from django.core.exceptions import ValidationError 

class ArtistSerializer(serializers.ModelSerializer):
	Stage_name = serializers.CharField(max_length=255, required=True)
	Social_link = serializers.URLField(max_length=255, required=True)
	class Meta:
		model = Artist
		fields = "__all__"