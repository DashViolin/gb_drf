from rest_framework.serializers import ModelSerializer

from userapp.models import CustomUser


class UserModelSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "first_name", "last_name", "email"]


class UserModelSerializerVer2(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "first_name", "last_name", "email", "is_superuser", "is_staff"]
