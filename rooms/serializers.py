from rest_framework import serializers
from . import models
from users.serializers import RelatedUserSerializer


class ReadRoomSerializer(serializers.ModelSerializer):
    user = RelatedUserSerializer()

    class Meta:
        model = models.Room
        fields = ("pk", "name", "price", "instant_book", "user")


class WriteRoomSerializer(serializers.ModelSerializer):
    class Meta:
        model = models.Room
        exclude = ("user", "modified", "created")

    def validate(self, data):
        if self.instance:
            # update
            check_in = data.get("check_in", self.instance.check_in)
            check_out = data.get("check_out", self.instance.check_out)
        else:
            # create
            check_in = data.get("check_in")
            check_out = data.get("check_out")

        if check_in == check_out:
            raise serializers.ValidationError("Not enough time between changes")

        return data

