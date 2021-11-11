from django.contrib.auth.models import User
from rest_framework import serializers
from .models import User

class UserShortcutSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ('user_id', 'user_name', 'email','department')