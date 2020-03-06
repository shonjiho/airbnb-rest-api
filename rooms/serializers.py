from rest_framework import serializers
from . import models
from users.serializers import RelatedUserSerializer


class RoomSerializer(serializers.ModelSerializer):
    user = RelatedUserSerializer()
    am_i_sexy = serializers.SerializerMethodField(method_name="get_am_i_sexy")

    class Meta:
        model = models.Room
        exclude = ("modified",)
        read_only_fields = ("user", "id", "created", "modified")

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

    def get_am_i_sexy(self, obj):
        request = self.context.get("request")
        if request:
            user = request.user
            if user.is_authenticated:
                return obj in user.favs.all()
        return False
