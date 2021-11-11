from rest_framework import serializers
from .models import BusSchedule

class BusSerializer(serializers.ModelSerializer):
    class Meta:
        model = BusSchedule
        fields = ('title', 'schedule_school', 'schedule_station')