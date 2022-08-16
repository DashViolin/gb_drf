from django.conf import settings
from rest_framework.pagination import LimitOffsetPagination
from rest_framework.viewsets import ModelViewSet

from todoapp.filters import ProjectFilter, ToDoFilter
from todoapp.models import Project, ToDo
from todoapp.serializers import ProjectModelSerializer, ToDoModelSerializer


class DefaultLimitOffsetPagination(LimitOffsetPagination):
    default_limit = settings.REST_FRAMEWORK.get("PAGE_SIZE", 5)


class ToDoLimitOffsetPagination(DefaultLimitOffsetPagination):
    default_limit = 10


# Мягкое удаление объектов реализовано на уровне менеджера моделей, так что метод delete переопределять не нужно.
class ProjectModelViewSet(ModelViewSet):
    serializer_class = ProjectModelSerializer
    queryset = Project.objects.filter(is_active=True)
    pagination_class = DefaultLimitOffsetPagination
    filterset_class = ProjectFilter


class ToDoModelViewSet(ModelViewSet):
    serializer_class = ToDoModelSerializer
    queryset = ToDo.objects.filter(is_active=True)
    pagination_class = ToDoLimitOffsetPagination
    filterset_class = ToDoFilter
