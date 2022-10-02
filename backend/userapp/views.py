from rest_framework.generics import mixins
from rest_framework.permissions import DjangoModelPermissions
from rest_framework.viewsets import GenericViewSet

from userapp.models import CustomUser
from userapp.serializers import UserModelSerializer, UserModelSerializerVer2


class UserModelViewSet(
    mixins.RetrieveModelMixin,
    mixins.ListModelMixin,
    mixins.UpdateModelMixin,
    GenericViewSet,
):
    serializer_class = UserModelSerializer
    queryset = CustomUser.objects.filter(is_active=True)
    permission_classes = [DjangoModelPermissions]

    def get_serializer_class(self):
        if self.request.version == "0.2":
            return UserModelSerializerVer2
        return UserModelSerializer
