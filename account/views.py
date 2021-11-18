from django.shortcuts import render
from rest_framework import status
from rest_framework.response import Response
from rest_framework.decorators import api_view, permission_classes
from rest_framework.permissions import IsAuthenticated
from .models import User
from django.forms.models import model_to_dict
from account.serializer import UserShortcutSerializer
import re
import json
from django.contrib import auth

def user_validation(data):
    user_id_check = User.objects.filter(user_id=data['user_id'])
    email_check1 = re.compile(
        r'[0-9a-zA-Z]+@[0-9a-zA-Z]+\.[0-9a-zA-Z]{2,}'
    ).search(data['email'])
    email_check2 = User.objects.filter(email=data['email']) #중복 체크
    
    if (user_id_check.exists()):
        return "USER_ID_EXIST"
    elif (email_check1 is None):
        return "EMAIL_INVAILD"
    elif (email_check2.exists()):
        return "EMAIL_EXIST"
    else:
        return "OK"
    
@api_view(['POST'])
def register(request):
    data = json.loads(request.body)
    required_fields = ('user_id', 'password','user_name', 'department', 'email')

    if not all(i in data for i in required_fields):
        return Response(
            {"message":"필수 양식을 입력해주세요."},
            status = status.HTTP_400_BAD_REQUEST
        )
    validation = user_validation(data)
    
    if (validation == "USER_ID_EXIST"):
        return Response(
            {"message":"이미 존재하는 아이디입니다."},
            status = status.HTTP_409_CONFLICT
        )
    elif (validation == "EMAIL_INVALID"):
        return Response(
            {"message":"정확한 이메일을 입력해주세요."},
            status = status.HTTP_400_BAD_REQUEST
        )
    elif (validation == "EMAIL_EXIST"):
        return Response(
            {"message":"이미 존재하는 이메일입니다."},
            status = status.HTTP_409_CONFLICT
        )
    else:
        user = User.objects.create_user(**data)
        return Response(
            model_to_dict(user),
            status = status.HTTP_201_CREATED
        )

@api_view(['GET', 'PUT'])
@permission_classes((IsAuthenticated,))
def info(request):
    user = request.user
    #data = request.data
    #email = request.user.email
    #user_name = request.user.user_name

    if (request.method == "GET"):
        result = UserShortcutSerializer(user)
        return Response(result.data, status=status.HTTP_200_OK)

@api_view(['POST'])
def logout(request):
    auth.logout(request)
    return Response(
        {"message":"로그아웃이 완료되었습니다."},
        status=status.HTTP_200_OK
    )