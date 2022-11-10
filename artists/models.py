from django.db import models
from users.models import *
class Artist(models.Model):
    Stage_name = models.CharField(max_length = 255 , null = False , unique = True)
    Social_link = models.URLField(max_length = 255 , null = False)
    User_id = models.OneToOneField(User, related_name = 'Artist', on_delete=models.CASCADE , null = True)
    def __str__(self):
        return self.Stage_name
    class Meta:
        db_table = 'Artist'
        ordering = ['Stage_name']
