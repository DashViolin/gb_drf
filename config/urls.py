from django.contrib import admin
from django.urls import include, path
from rest_framework.routers import DefaultRouter

from todoapp.views import ProjectModelViewSet, ToDoModelViewSet
from userapp.views import UserModelViewSet

router = DefaultRouter()
router.register("users", UserModelViewSet)
router.register("projects", ProjectModelViewSet)
router.register("todos", ToDoModelViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    # path('api-auth/', include('rest_framework.urls')),
    path("api/", include(router.urls)),
]
