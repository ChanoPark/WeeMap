# Generated by Django 3.2.9 on 2021-11-30 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0004_auto_20211130_1612'),
    ]

    operations = [
        migrations.AddField(
            model_name='buildinginfo',
            name='info_index',
            field=models.IntegerField(null=True, verbose_name='info_index'),
        ),
    ]
