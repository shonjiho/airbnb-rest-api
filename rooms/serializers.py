from rest_framework import serializers
from . import models
from users.serializers import TinyUserSerializer


class RoomSerializer(serializers.ModelSerializer):
    user = TinyUserSerializer()

    class Meta:
        model = models.Room
        fields = ("pk", "name", "price", "instant_book", "user")


class BigRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        exclude = ()

