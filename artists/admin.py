from django.contrib import admin

# Register your models here.
from django.contrib import admin
from .models import Artist
from albums.models import Album
from albums.form import AlbumForm
from django.db import models
class AlbumInline(admin.TabularInline):
    model = Album
    form = AlbumForm
    extra =  0


class ArtistAdmin(admin.ModelAdmin):
    def albums_count(self, Artist):
        return Artist.Album.filter(propriet = True).count()
    list_display = ('Stage_name', 'albums_count')
    fields = ["Stage_name" , "Social_link"]
    inlines = [AlbumInline]


admin.site.register(Artist, ArtistAdmin)
