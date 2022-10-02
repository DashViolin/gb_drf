# --- NESSESARY FOR VSCode's unittest tests discover (unittest_discovery.py) --- #
import os

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "config.settings")
import django
from django.conf import settings

if not settings.configured:
    django.setup()
# ------------------------------------------------------------------------------ #

from django.contrib.auth import get_user_model
from mixer.backend.django import mixer
from rest_framework import status
from rest_framework.test import APIRequestFactory, APITestCase

from .views import UserModelViewSet


class TestCustimUserViewSet(APITestCase):
    def setUp(self) -> None:
        self.new_first_name = "NewUserName"
        self.user_model = get_user_model()
        self.new_user = mixer.blend(self.user_model)
        self.admin = self.user_model.objects.get(username="admin")
        return super().setUp()

    def test_get_users_unauthorized_by_request_factory(self):
        factory = APIRequestFactory()
        request = factory.get("/api/users/")
        view = UserModelViewSet.as_view({"get": "list"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_users_unauthorized(self):
        response = self.client.get(f"/api/users/{self.new_user.id}/")
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_users(self):
        self.client.force_login(self.admin)
        response = self.client.get(f"/api/users/{self.new_user.id}/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_put_users(self):
        self.client.force_login(self.admin)
        response = self.client.put(
            f"/api/users/{self.new_user.id}/",
            {
                "username": self.new_user.username,
                "first_name": self.new_first_name,
            },
        )
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        modified_user = self.user_model.objects.get(id=self.new_user.id)
        self.assertEqual(modified_user.first_name, self.new_first_name)
