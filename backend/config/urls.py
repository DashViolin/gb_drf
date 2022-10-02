from django.contrib import admin
from django.urls import include, path, re_path
from django.views.decorators.csrf import csrf_exempt
from django.views.generic import TemplateView
from drf_yasg import openapi
from drf_yasg.views import get_schema_view as yasg_get_schema_view
from graphene_django.views import GraphQLView
from rest_framework.authtoken import views
from rest_framework.permissions import AllowAny
from rest_framework.routers import DefaultRouter
from rest_framework.schemas import get_schema_view as drf_get_schema_view
from rest_framework_simplejwt.views import TokenObtainPairView, TokenRefreshView, TokenVerifyView

from todoapp.views import ProjectModelViewSet, ToDoModelViewSet
from userapp.views import UserModelViewSet

drf_schema_view = drf_get_schema_view(
    title="Task manager OpenAPI Schema", description="Main API endpoints.", version="0.1"
)

yasg_schema_view = yasg_get_schema_view(
    openapi.Info(
        title="Task manager OpenAPI Schema",
        default_version="0.1",
        description="Project API documentation.",
        contact=openapi.Contact(email="admin@admin.local"),
        license=openapi.License(name="MIT License"),
    ),
    public=True,
    permission_classes=[AllowAny],
)


router = DefaultRouter()
router.register("users", UserModelViewSet)
router.register("projects", ProjectModelViewSet)
router.register("todos", ToDoModelViewSet)

urlpatterns = [
    path("admin/", admin.site.urls),
    path(
        "openapi/swagger-ui/",
        TemplateView.as_view(template_name="swagger-ui.html", extra_context={"schema_url": "schema-openapi-drf"}),
        name="swagger-ui",
    ),  # Swagger UI без сторонних билиотек (задание со *):
    path("openapi/drf/", drf_schema_view, name="schema-openapi-drf"),
    path("openapi/swagger/", yasg_schema_view.with_ui("swagger", cache_timeout=0), name="schema-swagger-ui"),
    path("openapi/redoc/", yasg_schema_view.with_ui("redoc", cache_timeout=0), name="schema-redoc"),
    re_path(
        r"^openapi/swagger(?P<format>\.json|\.yaml)$", yasg_schema_view.without_ui(cache_timeout=0), name="schema-json"
    ),
    path("api-auth/", include("rest_framework.urls")),
    path("api-token-auth/", views.obtain_auth_token),
    path("api-jwt-token/", TokenObtainPairView.as_view(), name="token_obtain_pair"),
    path("api-jwt-token/refresh/", TokenRefreshView.as_view(), name="token_refresh"),
    path("api-jwt-token/verify/", TokenVerifyView.as_view(), name="token_verify"),
    path("api/", include(router.urls)),
    path("graphql/", csrf_exempt(GraphQLView.as_view(graphiql=True))),
]
