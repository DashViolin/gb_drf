from django_filters import rest_framework as filters

from todoapp.models import Project, ToDo


class ProjectFilter(filters.FilterSet):
    title = filters.CharFilter(lookup_expr="contains")

    class Meta:
        model = Project
        fields = ["title"]


class ToDoFilter(filters.FilterSet):
    text = filters.CharFilter(lookup_expr="contains")
    created = filters.DateFromToRangeFilter()
    project = filters.CharFilter(field_name="project__title", lookup_expr="contains")

    class Meta:
        model = ToDo
        fields = ["text", "created"]
