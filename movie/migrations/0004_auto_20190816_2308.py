# Generated by Django 2.2.4 on 2019-08-16 17:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movie', '0003_movie_slug'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='status',
            field=models.CharField(choices=[('RA', 'RECENTLY ADDED'), ('MW', 'MOST WATCHED'), ('TR', 'TOP RATED')], max_length=2),
        ),
    ]
