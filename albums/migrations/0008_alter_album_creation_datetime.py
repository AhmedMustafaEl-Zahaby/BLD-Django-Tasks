# Generated by Django 4.1.3 on 2022-11-01 17:20

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0007_alter_album_creation_datetime'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='creation_datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 1, 19, 20, 42, 936062)),
        ),
    ]