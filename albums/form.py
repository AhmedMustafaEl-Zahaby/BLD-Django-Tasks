
from django import forms
from django.forms import ModelForm, ValidationError
from .models import *


def validate_Album(self, Album):
    if Album.Song.count() < 1:
        raise ValidationError('Album must have at least one song')


class AlbumForm(forms.ModelForm):
    propriet = forms.BooleanField(required=False,help_text="Approve the album if its name is not explicit")
    class Meta:
        model = Album
        fields = ['name', "creation_datetime" , "release_datetime" , "cost" , "propriet" , "artist"]
        validators = [validate_Album]


class SongForm(forms.ModelForm):
    class Meta:
        model = Song
        fields = "__all__"