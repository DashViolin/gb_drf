from rest_framework.serializers import ModelSerializer

from todoapp.models import Project, ToDo
from userapp.serializers import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):
    users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        exclude = ["is_active", "created", "updated"]


class ToDoModelSerializer(ModelSerializer):
    author = UserModelSerializer()

    class Meta:
        model = ToDo
        exclude = ["is_active", "updated"]
