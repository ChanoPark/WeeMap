from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import status
from rest_framework.response import Response
from tab.models import BusSchedule
import json
#식단표 크롤링
import requests
from bs4 import BeautifulSoup

#셔틀할 때 쓸라고 가져왔으나 미사용중
from tab.serializer import BusSerializer
from django.forms.models import model_to_dict

#셔틀 버스 시간표
@api_view(['POST'])
def getBus(request):
    data = json.loads(request.body)
    day=data.get('is_holiday')

    if (day == 1): #월~목
        weekend = BusSchedule.objects.exclude(is_holiday=3).values()
        return Response(weekend, status=status.HTTP_200_OK)
    #elif (day['is_holiday'] == 2): #금
    #    friday = BusSchedule.objects.filter(is_holiday=1).values()
    #    return Response(friday, status=status.HTTP_200_OK)
    else: #일요일
        sunday = BusSchedule.objects.filter(is_holiday=3).values()
        return Response(sunday, status=status.HTTP_200_OK)


    #result = BusSchedule.objects.all()
    #serializer = BusSerializer(result, many=True)
    #return Response(request.data, status=status.HTTP_200_OK) #{is_holiday : 1}
    #return Response(serializer.data, status=status.HTTP_200_OK) #시간표 싹 긁어옴

#금주의 식단표
@api_view(['POST'])
def getMenu(request):
    url = requests.get('https://sejong.korea.ac.kr/campuslife/facilities/dining/weeklymenu')
    raw = url.text
    html = BeautifulSoup(raw, 'html.parser')
    infos = html.select('.buttonGo > a')
    
    teacher_restaurant_list = infos[0].get_attribute_list('href')
    student_restaurant_list = infos[1].get_attribute_list('href')

    teacher_restaurant = "https://sejong.korea.ac.kr" + teacher_restaurant_list[0]
    student_restaurant = "https://sejong.korea.ac.kr" + student_restaurant_list[0]

    data = json.loads(request.body)
    restaurant_type=data.get('restaurant_type')
    
    # 0=교직원식당, 1=학생식당
    if(restaurant_type == 0):
        return Response(teacher_restaurant, status=status.HTTP_200_OK)
    else:
        return Response(student_restaurant, status=status.HTTP_200_OK)