from .serializers import ProfileModelSerializer
from rest_framework import generics
from rest_framework import permissions
from accounts.models import UserProfile
from rest_framework.views import APIView


class ProfilesListApiView(generics.ListAPIView):
    serializer_class = ProfileModelSerializer
    permission_classes = [permissions.IsAuthenticated]
    queryset = UserProfile.objects.all()

class HelloView(APIView):
    permission_classes = (permissions.IsAuthenticated,)             
    def get(self, request):
        content = {'message': 'Hello, World!'}
        return Response(content)


class GetUserProfileListApiView(generics.ListAPIView):
    serializer_class = ProfileModelSerializer
    permission_classes = [permissions.IsAuthenticated]       

    def get_queryset(self):
        queryset = UserProfile.objects.filter(user=self.request.user)
        return queryset



