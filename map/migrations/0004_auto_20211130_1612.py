# Generated by Django 3.2.9 on 2021-11-30 16:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('map', '0003_map_building_info'),
    ]

    operations = [
        migrations.CreateModel(
            name='BuildingInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('building_id', models.IntegerField(verbose_name='building_id')),
                ('info_name', models.CharField(max_length=30, null=True, verbose_name='info_name')),
                ('info_location', models.CharField(max_length=20, null=True, verbose_name='info_location')),
                ('info_explain', models.CharField(max_length=200, null=True, verbose_name='info_explain')),
            ],
        ),
        migrations.RemoveField(
            model_name='map',
            name='building_info',
        ),
        migrations.AddField(
            model_name='map',
            name='building_num',
            field=models.IntegerField(null=True, verbose_name='building_num'),
        ),
    ]
