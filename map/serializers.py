from rest_framework import serializers
from .models import Map

class MapSerializer(serializers.ModelSerializer):
    class Meta:
        model = Map
        fields = ('id', 'latitude', 'longitude', 'building_name', 'is_building')

class ImageSerializer(serializers.ModelSerializer):
    building_image = serializers.ImageField(use_url=True)
    class Meta:
        model = Map
        fields = ('is_building','building_image')