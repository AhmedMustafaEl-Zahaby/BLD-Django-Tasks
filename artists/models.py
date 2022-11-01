
from django.db import models
class Artist(models.Model):
    Stage_name = models.CharField(max_length = 255 , null = False , unique = True)
    Social_link = models.URLField(max_length = 255 , null = False)
    def __str__(self):
        return self.Stage_name
    class Meta:
        db_table = 'Artist'
        ordering = ['Stage_name']
