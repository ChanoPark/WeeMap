from django.shortcuts import render
from django.forms.models import model_to_dict
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .models import Map, Booth
from map.serializers import MapSerializer
import json


@api_view(['POST'])
def rendering_map(request):
    building = Map.objects.all().values()

    return Response(building, status=status.HTTP_200_OK)

@api_view(['POST'])
def register_booth(request):
    data = json.loads(request.body)
    required_fields = ('latitude', 'longitude', 'building_name', 'start_date', 'end_date', 'booth_host', 'booth_explain')

    if not all(i in data for i in required_fields):
        return Response(
            {"message": "양식을 모두 입력해주세요."},
            status = status.HTTP_400_BAD_REQUEST
        )
    
    add_map = Map.objects.create(
        latitude = data["latitude"],
        longitude = data["longitude"],
        building_name = data["building_name"]
    )
    
    add_booth = Booth.objects.create(
        start_date = data["start_date"],
        end_date = data["end_date"],
        booth_host = data["booth_host"],
        booth_explain = data["booth_explain"],
        map_id = add_map.id
    )

    #생성은 되는데 뭘 알려줘야되지??
    return Response(model_to_dict(add_booth), status=status.HTTP_200_OK)