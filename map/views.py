from django.shortcuts import render
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Map, Booth, BuildingInfo, UserLocation
from map.serializers import MapSerializer, ImageSerializer
import json
import re
from operator import itemgetter
from django.utils import timezone
from django.views.decorators.csrf import csrf_exempt
from haversine import haversine

@api_view(['POST'])
def rendering_map(request):
    building = Map.objects.all().values()
    #serializers = MapSerializer(building)
    return Response(building, status=status.HTTP_200_OK)
    #return Response(serializers.data, status=status.HTTP_200_OK)

def map_validation(data):
    map_position_check = Map.objects.filter(latitude=data['latitude'], longitude=data['longitude'])
    start_check = re.compile(r'[0-9]+-[0-9]+-[0-9]').search(data['start_date'])
    end_check = re.compile(r'[0-9]+-[0-9]+-[0-9]').search(data['end_date'])

    if (map_position_check.exists()):
        return "POSITION_EXIST"
    elif (start_check is None):
        return "START_INVALID"
    elif (end_check is None):
        return "END_INVALID"

@api_view(['POST'])
def register_booth(request):
    data = json.loads(request.body)
    required_fields = ('latitude', 'longitude', 'booth_name', 'start_date', 'end_date', 'booth_host', 'booth_explain')
##########################----양식(building_name -> booth_name) 프론트에서 바꿔야됌!!!!---########################################
    if not all(i in data for i in required_fields):
        return Response(
            {"message": "양식을 모두 입력해주세요."},
            status = status.HTTP_400_BAD_REQUEST
        )
    validation = map_validation(data)

    if(validation == "LATITUDE_EXIST"):
        return Response(
            {"message":"해당 위치에 부스가 존재합니다."},
            status=status.HTTP_409_CONFLICT
        )
    elif (validation == "START_INVAILD"):
        return Response(
            {"message":"시작 날짜를 양식에 맞춰 입력해주세요."},
            status=status.HTTP_400_BAD_REQUEST
        )
    elif (validation == "END_INVAILD"):
        return Response(
            {"message":"종료 날짜를 양식에 맞춰 입력해주세요."},
            status=status.HTTP_400_BAD_REQUEST
        )
    
    add_map = Map.objects.create(
        latitude = data["latitude"],
        longitude = data["longitude"],
        building_name = data["booth_name"],
        is_building = False
    )
    
    add_booth = Booth.objects.create(
        start_date = data["start_date"],
        end_date = data["end_date"],
        booth_name = data["booth_name"],
        booth_host = data["booth_host"],
        booth_explain = data["booth_explain"],
        map_id = add_map.id
    )

    return Response(model_to_dict(add_booth), status=status.HTTP_201_CREATED)

api_view(['POST'])
def delete_booth(request):
    data = json.loads(request.body)
    required_fields = ('building_name')
    if (not i in data for i in required_fields):
        return Response(
            {"message" : "부스를 삭제하려면 부스 이름이 입력되어야 합니다."},
            status=status.HTTP_400_BAD_REQUEST
        )
    building_name = Booth.objects.filter(booth_name=data['building_name'])
    if (building_name==data['building_name']):
        Map.objects.filter(id=building_name)
        return Response(
            {"message":"삭제가 완료되었습니다.."},
            status=status.HTTP_200_OK
        )
    else:
        return Response(
            {"message":"일치하는 부스가 없습니다."},
            status=status.HTTP_400_BAD_REQUEST
        )

@api_view(['POST'])
@csrf_exempt
def marker_info(request):
    data = json.loads(request.body)
    
    if (data['is_building']==1 and 'id' in data):
        info = BuildingInfo.objects.filter(building_id=data['id']).values()
        return Response(info, status=status.HTTP_200_OK)
    elif (data['is_building']==0 and 'id' in data):
        info = Booth.objects.filter(map_id=data['id']).values()
        return Response(info, status=status.HTTP_200_OK)
    else:
        return Response({"Message":"해당 정보의 ID값이 없거나 올바르지 않습니다."},
        status=status.HTTP_400_BAD_REQUEST)

def auto_delete_booth():
    booth = Booth.objects.all().values('end_date', 'map_id')
    date = []
    for i in booth: #입력된 날짜 포맷 ['연','월','일']로 변환
        date.append([i['end_date'].split('-'), i['map_id']])
    print(date)
    date_int = []
    temp = []
    idx = 0
    for k in date: #문자열 -> 정수형 캐스팅 (올바른 정렬을 위해서)
        temp.append(list(map(int,k[0])))
        date_int.append([temp[idx], k[1]])
        idx+=1
    del temp, date, idx
    print(date_int)
    date_int.sort(key=itemgetter(0)) #정렬
    print(date_int)

    for item in date_int:   #연도, 달이 이번 연도(달) 이하이면서 요일이 지나면 삭제
        if (item[0][0] <= timezone.now().year and item[0][1] <= timezone.now().month and item[0][2] < timezone.now().day):
            finished_booth = Booth.objects.get(map_id=item[1])
            print(finished_booth)
            finished_booth.delete()
    print(timezone.now, "해당 날짜가 지난 부스가 삭제되었습니다.")

@api_view(['POST'])
def cal_hotplace(request):
    latitude = UserLocation.objects.all().values('user_latitude')
    longitude = UserLocation.objects.all().values('user_longitude')
    
    result = [0]*len(latitude)
    lati = []
    longi = []
    idx = 0

    for i, j in zip(latitude, longitude):
        lati.append(i['user_latitude'])
        longi.append(j['user_longitude'])
        
    for t, g in zip(lati, longi):
        idx2 = 0
        a = (t, g)
        for t2, g2 in zip(lati, longi):
            b = (t2, g2)
            if (haversine(a, b) < 0.01): #거리가 10m 미만
                result[idx] += 1
            idx2+=1
        idx+=1
    
    max_idx = result.index(max(result))

    Map.objects.filter(is_building=2).update(latitude=lati[max_idx])
    Map.objects.filter(is_building=2).update(longitude=longi[max_idx])
    
    return Response(status.HTTP_200_OK)