from rest_framework.response import Response
from rest_framework.permissions import IsAuthenticated
from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework import status
from .models import User
from .serializers import ReadUserSerializer, WriteUserSerializer


class MeView(APIView):
    permission_classes = [IsAuthenticated]

    def get(self, request):
        if request.user.is_authenticated:
            return Response(ReadUserSerializer(request.user).data)
        return Response(status.HTTP_404_NOT_FOUND)

    def put(self, request):
        serializers = WriteUserSerializer(request.user, data=request.data, partial=True)
        if serializers.is_valid():
            serializers.save()
            return Response()
        else:
            return Response(serializers.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(["GET"])
def user_detail(request, pk):
    try:
        user = User.objects.get(pk=pk)
        return Response(ReadUserSerializer(user).data)
    except User.DoesNotExist:
        return Response(status.HTTP_404_NOT_FOUND)
