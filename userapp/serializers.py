from rest_framework.serializers import ModelSerializer

from .models import CustomUser

# from rest_framework.serializers import HyperlinkedModelSerializer

# class UserModelSerializer(HyperlinkedModelSerializer):
class UserModelSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["id", "username", "first_name", "last_name", "email"]
