from rest_framework.serializers import ModelSerializer, StringRelatedField

from todoapp.models import Project, ToDo
from userapp.serializers import UserModelSerializer


class ProjectModelSerializer(ModelSerializer):
    users = UserModelSerializer(many=True)

    class Meta:
        model = Project
        exclude = ["is_active", "created", "updated"]


class ToDoModelSerializer(ModelSerializer):
    author = UserModelSerializer()
    project = StringRelatedField()

    class Meta:
        model = ToDo
        exclude = ["is_active", "created", "updated"]
