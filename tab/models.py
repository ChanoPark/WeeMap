from django.db import models

#셔틀 시간표 모델
class BusSchedule(models.Model):
    title = models.IntegerField(
        verbose_name = 'bus_schedule_index'
    )
    schedule_school = models.CharField(
        verbose_name = 'bus_schedule_school',
        max_length=8,
        null=True
    )
    schedule_station = models.CharField(
        verbose_name = 'bus_schedule_station',
        max_length=8,
        null=True
    )
    # 1=평일, 2=금요일, 3=일요일 -> 1=평일, 3=일요일
    is_holiday = models.IntegerField(
        verbose_name = 'is_holiday',
    )