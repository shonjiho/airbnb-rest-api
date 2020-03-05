from rest_framework.decorators import api_view
from rest_framework.views import APIView
from rest_framework.generics import ListAPIView, RetrieveAPIView

from rest_framework.response import Response
from .serializers import RoomSerializer, BigRoomSerializer
from .models import Room

# function view API
@api_view(
    ["GET",]
)
def list_rooms(request):
    rooms = Room.objects.all()
    serialized_rooms = RoomSerializer(rooms, many=True)
    return Response(data=serialized_rooms.data)


# generic view api
class ListRoomsView(ListAPIView):
    queryset = Room.objects.all()
    serializer_class = RoomSerializer


class SeeRoomView(RetrieveAPIView):
    queryset = Room.objects.all()
    serializer_class = BigRoomSerializer
    pass
