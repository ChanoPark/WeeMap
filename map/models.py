from django.db import models

class Map(models.Model): #메인 지도 렌더링을 위한 기본 건물 정보
    latitude = models.DecimalField( #위도
        verbose_name = 'latitude',
        max_digits= 30,
        decimal_places = 6,
    )
    longitude = models.DecimalField( #경도
        verbose_name = 'longitude',
        max_digits= 30,
        decimal_places = 6,
    )
    building_name = models.CharField(
        verbose_name = 'building_name',
        max_length = 30
    )
    is_building = models.IntegerField( #0=부스, 1=건물, 2=핫플
        verbose_name = 'is_building',
        default=0
    )
    building_image = models.ImageField( #파일 다루기 위해 pillow 설치
        verbose_name = 'building_image',
        default = 'media/building/default.jpeg',
        upload_to="building",
        null = True,
        blank = True
    )
    building_num = models.IntegerField(
        verbose_name='building_num',
        null=True
    )

class BuildingInfo(models.Model):
    building_id = models.IntegerField( 
        verbose_name='building_id',
        unique=False
    )
    info_name = models.CharField(
        verbose_name='info_name',
        max_length=30,
        null=True,
        unique=False
    )
    info_location = models.CharField(
        verbose_name='info_location',
        max_length=20,
        null=True,
        unique=False
    )
    info_explain = models.CharField(
        verbose_name='info_explain',
        max_length=200,
        null=True
    )
    info_index = models.IntegerField( # 1=건물내에 있는 학과 / 2=PL센터와 같은 시설
        verbose_name='info_index',
        unique=False,
        null=True
    )


class Booth(models.Model): #행사 부스 설치를 위한 정보 관리
    map_id = models.IntegerField(
        unique=True
        #Map,
        #on_delete=models.CASCADE,
        #related_name='map',
        #db_column='id',
        #default=1
    )
    """
    start_date = models.DateTimeField(
        verbose_name = 'start_date',
        auto_now_add = False,
        auto_now = False
    )
    end_date = models.DateTimeField(
        verbose_name = 'end_date',
        auto_now_add = False,
        auto_now = False
    )
    """
    start_date = models.CharField(
        verbose_name = 'start_date',
        max_length = 15
    )
    end_date = models.CharField(
        verbose_name = 'end_date',
        max_length = 15
    )
    booth_host = models.CharField( #주최자 -> 소속
        verbose_name = 'booth_host',
        max_length = 10
    )
    booth_name = models.CharField(
        verbose_name = 'booth_name',
        max_length = 30
    )
    booth_explain = models.TextField(
        verbose_name = 'booth_explain',
        max_length = 150
    )

class UserLocation(models.Model):
    user_latitude = models.DecimalField( #위도
        verbose_name = 'latitude',
        max_digits= 30,
        decimal_places = 6,
        unique = False
    )
    user_longitude = models.DecimalField( #경도
        verbose_name = 'longitude',
        max_digits= 30,
        decimal_places = 6,
        unique = False
    )