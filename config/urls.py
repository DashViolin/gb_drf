from django.contrib import admin
from django.urls import include, path
from rest_framework.authtoken import views
from rest_framework.routers import DefaultRouter
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from todoapp.views import ProjectModelViewSet, ToDoModelViewSet
from userapp.views import UserModelViewSet

router = DefaultRouter()
router.register("users", UserModelViewSet)
router.register("projects", ProjectModelViewSet)
router.register("todos", ToDoModelViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path("api-auth/", include("rest_framework.urls")),
    path("api-token-auth/", views.obtain_auth_token),
    path("api/jwt-token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api/jwt-token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api/jwt-token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/", include(router.urls)),
]
