# Generated by Django 3.2.9 on 2021-11-29 23:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='map',
            name='building_image',
            field=models.ImageField(blank=True, default='media/building/default.jpeg', null=True, upload_to='building', verbose_name='building_image'),
        ),
    ]