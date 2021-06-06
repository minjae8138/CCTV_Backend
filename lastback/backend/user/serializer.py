from rest_framework import serializers

from user.models import User


class UserSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'Email', 'Ip']


class InfoSerializer(serializers.ModelSerializer):
    class Meta:
        model = User
        fields = ['name', 'Email', 'Ip', 'makeDate']
