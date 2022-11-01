from email.policy import default
from django.db import models
from datetime import  datetime
from artists.models import Artist
class Album(models.Model):
    name = models.CharField(max_length = 255 , default="New Album")
    creation_datetime = models.DateTimeField(default=datetime.now())
    release_datetime = models.DateTimeField(blank = False)
    cost = models.IntegerField(null = True)
    propriet = models.BooleanField(default = False)
    artist = models.ForeignKey(Artist , related_name = 'Album' , on_delete = models.CASCADE)

    def __str__(self):
        return self.name

    class Meta:
        db_table = 'Album'
