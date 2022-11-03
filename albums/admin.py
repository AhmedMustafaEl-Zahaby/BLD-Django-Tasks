from django.contrib import admin
from .models import *
from .form import AlbumForm
from django.forms import ModelForm, ValidationError


def validate_Album(self, Album):
    if Album.Song.count() < 1:
        raise ValidationError('Album must have at least one song to delete')

class SongInLine(admin.TabularInline):
    model = Song
    extra = 1

class AlbumAdmin(admin.ModelAdmin):
    form = AlbumForm
    readonly_fields= ('creation_datetime',)
    list_display = ('name', "creation_datetime" , "release_datetime" , "cost" , "propriet" , "artist" , "songs_count")
    fields = ['name', "creation_datetime" , "release_datetime" , "cost" , "propriet" , "artist"]
    inlines = [SongInLine]

    def save_model(self, request, obj, form, change):
        validate_Album(self , obj)
        super().save_model(request, obj, form, change)
    
    def songs_count(self , Album):
        return Album.Song.count()

class SongAdmin(admin.ModelAdmin):
    
    fields = ['name', 'album', 'image', 'audio']

admin.site.register(Album, AlbumAdmin , form=AlbumForm)
admin.site.register(Song, SongAdmin)
