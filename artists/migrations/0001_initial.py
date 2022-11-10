# Generated by Django 4.1.3 on 2022-11-10 10:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Artist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Stage_name', models.CharField(max_length=255, unique=True)),
                ('Social_link', models.URLField(max_length=255)),
            ],
            options={
                'db_table': 'Artist',
                'ordering': ['Stage_name'],
            },
        ),
    ]
