from rest_framework.viewsets import ModelViewSet

from .models import CustomUser
from .serializers import UserModelSerializer


class UserModelViewSet(ModelViewSet):
    serializer_class = UserModelSerializer
    queryset = CustomUser.objects.all()
