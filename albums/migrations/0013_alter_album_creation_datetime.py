# Generated by Django 4.1.3 on 2022-11-02 12:59

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('albums', '0012_alter_album_creation_datetime_alter_album_propriet'),
    ]

    operations = [
        migrations.AlterField(
            model_name='album',
            name='creation_datetime',
            field=models.DateTimeField(default=datetime.datetime(2022, 11, 2, 14, 59, 8, 794058)),
        ),
    ]