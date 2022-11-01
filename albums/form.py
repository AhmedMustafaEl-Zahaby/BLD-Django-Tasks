
from django import forms
from .models import Album
class AlbumForm(forms.ModelForm):
    propriet = forms.BooleanField(required=False,help_text="Approve the album if its name is not explicit")
    class Meta:
        model = Album
        fields = ['name', "creation_datetime" , "release_datetime" , "cost" , "propriet" , "artist"]