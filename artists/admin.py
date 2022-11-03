from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Artist
from albums.models import Album
from albums.form import AlbumForm
from django.db import models

class ArtistAdmin(admin.ModelAdmin):
    def approved_albums(self, Artist):
        return Artist.Album.filter(propriet = True).count()
    list_display = ('Stage_name', 'approved_albums')
    fields = ["Stage_name" , "Social_link"]


admin.site.register(Artist, ArtistAdmin)
