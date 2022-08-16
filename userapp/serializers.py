from rest_framework.serializers import ModelSerializer

from userapp.models import CustomUser

# from rest_framework.serializers import HyperlinkedModelSerializer

# class UserModelSerializer(HyperlinkedModelSerializer):
class UserModelSerializer(ModelSerializer):
    class Meta:
        model = CustomUser
        fields = ["username", "first_name", "last_name", "email"]
