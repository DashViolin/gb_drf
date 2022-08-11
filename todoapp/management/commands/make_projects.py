import json

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from todoapp.models import Project


class Command(BaseCommand):
    help = "Use this command to create some test projects"

    def handle(self, *args, **options):
        test_projects_file = settings.DATA_DIR / "test_data" / "test_projects.json"
        if test_projects_file.exists:
            print("--> Create projects <--")
            all_users = get_user_model().objects.all()
            with open(test_projects_file) as f:
                test_projects = json.load(f)
            for index, test_project in enumerate(test_projects):
                users = all_users[index + 1 : index + 3]
                project = Project(**test_project)
                project.save()
                project.users.add(*users)
                print(f" -> Project \"{test_project['title']}\" created")
