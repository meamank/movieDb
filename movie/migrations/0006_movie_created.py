# Generated by Django 2.2.4 on 2019-08-17 06:11

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0005_movie_movie_trailer'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
