from django.db import models
from datetime import  datetime
from artists.models import Artist
from django.core.validators import FileExtensionValidator
from ImageKit.models import ImageSpecField
from django.dispatch import receiver
from django.db.models.signals import post_save, pre_save
from .tasks import *
from django.utils.text import slugify

class AlbumManager(models.Manager):
    def get_queryset(self):
        return super().get_queryset().filter(propriet = True)


class Album(models.Model):
    name = models.CharField(max_length = 255 , default="New Album")
    creation_datetime = models.DateTimeField(default=datetime.now())
    release_datetime = models.DateTimeField(blank = False)
    cost = models.IntegerField(null = True)
    propriet = models.BooleanField(default = False)
    artist = models.ForeignKey(Artist , related_name = 'Album' , on_delete = models.CASCADE)
    objects = AlbumManager()


    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Album'

class Song(models.Model):
    album = models.ForeignKey(Album , related_name = 'Song' , on_delete = models.CASCADE)
    name = models.CharField(max_length = 255 , default = album.name)
    image = models.ImageField(upload_to='songs/images')
    image_thumbnail = ImageSpecField(source='image', format='JPEG')
    audio = models.FileField(upload_to='songs/audio', null = False , validators=[FileExtensionValidator(allowed_extensions=['mp3', 'wav'])])

    def __str__(self):
        return self.name
    
    class Meta:
        db_table = 'Song'

@receiver(post_save, sender=Album)
def album_post_save(sender, instance, created, *args, **kwargs):
    if created:
        send_mail_task.delay(instance.name, instance.artist.id)


@receiver(pre_save, sender=Song)
def song_pre_save(sender, instance, *args, **kwargs):
    if len(instance.name.strip()) == 0:
        instance.name = slugify(instance.album.name)