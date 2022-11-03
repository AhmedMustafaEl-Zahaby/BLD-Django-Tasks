from django import forms
from .models import *
class ArtistForm(forms.ModelForm):


    class Meta:
        model = Artist
        fields = ["Stage_name" , "Social_link"]