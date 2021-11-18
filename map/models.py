from django.db import models

class Map(models.Model): #메인 지도 렌더링을 위한 기본 건물 정보
    def create_map(self, latitude, longitude, building_name): #start_date, end_date, booth_host, booth_explain
        booth = self.objects.create(
            latitude = latitude,
            longitude = longitude,
            building_name = building_name,
            is_building = False,
        )
        return booth

    #id = models.AutoField(
    #    verbose_name = 'id',
    #    primary_key=True
    #)
    latitude = models.DecimalField( #위도
        verbose_name = 'latitude',
        max_digits= 30,
        decimal_places = 6,
        unique = False
    )
    longitude = models.DecimalField( #경도
        verbose_name = 'longitude',
        max_digits= 30,
        decimal_places = 6,
        unique = False
    )
    building_name = models.CharField(
        verbose_name = 'building_name',
        max_length = 30
    )
    is_building = models.BooleanField( #True=건물, False=부스
        verbose_name = 'is_building',
        default = True
    )
    """ #이미지 일단 잠깐 주석
    building_image = models.ImageField( #파일 다루기 위해 pillow 설치
        verbose_name = 'building_image',
        default = 'media/building/default.jpeg',
        upload_to="building",
        null = True,
        blank = True
    )
    """

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