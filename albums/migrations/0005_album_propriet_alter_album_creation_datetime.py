# Generated by Django 4.1.3 on 2022-11-01 16:54

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0004_alter_album_creation_datetime'),
    ]

    operations = [
        migrations.AddField(
            model_name='album',
            name='propriet',
            field=models.BooleanField(default=False),
        ),
        migrations.AlterField(
            model_name='album',
            name='creation_datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 1, 18, 54, 52, 558577)),
        ),
    ]