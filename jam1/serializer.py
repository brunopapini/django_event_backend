from django.contrib.auth.models import User, Group
from rest_framework import serializers
from jam1.models import *


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = "__all__"


class GroupSerializer(serializers.ModelSerializer):
	class Meta:
		model = Group
		fields = ['url', 'name']


class EventSerializer(serializers.ModelSerializer):
    class Meta:
        model = Event
        fields = "__all__"