from django.contrib import admin
from .models import Album
from .form import AlbumForm
class AlbumAdmin(admin.ModelAdmin):
    readonly_fields= ('creation_datetime',)
    list_display = ('name', "creation_datetime" , "release_datetime" , "cost" , "propriet" , "artist")
    fields = ['name', "creation_datetime" , "release_datetime" , "cost" , "propriet" , "artist"]

admin.site.register(Album, AlbumAdmin , form=AlbumForm)
