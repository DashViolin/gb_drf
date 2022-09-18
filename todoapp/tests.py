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
from rest_framework.test import APILiveServerTestCase, APIRequestFactory, APITestCase, force_authenticate

from .models import Project, ToDo
from .views import ToDoModelViewSet


class TestToDoViewSet(APITestCase):
    def setUp(self) -> None:
        self.new_task_text = "NewTextValue"
        self.user_model = get_user_model()
        self.new_user = mixer.blend(self.user_model)
        self.admin = self.user_model.objects.get(username="admin")
        self.new_project = mixer.blend(Project)
        self.new_task = mixer.blend(ToDo)
        return super().setUp()

    def test_get_todos_unauthorized_by_request_factory(self):
        factory = APIRequestFactory()
        request = factory.get("/api/todos/")
        view = ToDoModelViewSet.as_view({"get": "list"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_get_todo_by_request_factory(self):
        factory = APIRequestFactory()
        request = factory.get("/api/todos/")
        force_authenticate(request, self.admin)
        view = ToDoModelViewSet.as_view({"get": "list"})
        response = view(request)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_get_todos(self):
        self.client.force_login(self.admin)
        response = self.client.get(f"/api/users/")
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_patch_todos_unauthorized(self):
        response = self.client.put(f"/api/todos/{self.new_task.id}/", {"text": self.new_task_text})
        self.assertEqual(response.status_code, status.HTTP_403_FORBIDDEN)

    def test_patch_todos(self):
        self.client.force_login(self.admin)
        response = self.client.patch(f"/api/todos/{self.new_task.id}/", {"text": self.new_task_text})
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        task = ToDo.objects.get(id=self.new_task.id)
        self.assertEqual(task.text, self.new_task_text)


class TestProjectsViewSet(APILiveServerTestCase):
    def setUp(self) -> None:
        self.user_model = get_user_model()
        self.new_user = mixer.blend(self.user_model)
        self.admin = self.user_model.objects.get(username="admin")
        self.new_project = mixer.blend(Project)
        self.new_task = mixer.blend(ToDo)
        return super().setUp()

    def test_create_project(self):
        self.client.force_login(self.admin)
        response = self.client.post(
            f"/api/projects/",
            {
                "users": [
                    self.new_user.id,
                ],
                "title": "new_test_project",
                "repo": "http://someserver.com/somerepo",
            },
        )
        self.assertEqual(response.status_code, status.HTTP_201_CREATED)
