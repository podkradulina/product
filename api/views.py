from rest_framework import viewsets

from api.models import ApiUser
from api.serializers import UserSerializer

# Create your views here.
class UserModelViewSet(viewsets.ModelViewSet):
    queryset = ApiUser.objects.all()
    http_method_names = ['post','path','get']
    serializer_class = UserSerializer