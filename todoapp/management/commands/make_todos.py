import json
from itertools import cycle

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand

from todoapp.models import Project, ToDo


class Command(BaseCommand):
    help = "Use this command to create some test projects"

    def handle(self, *args, **options):
        test_todos_file = settings.DATA_DIR / "test_data" / "test_todos.json"
        if test_todos_file.exists:
            print("--> Create ToDos <--")
            authors = get_user_model().objects.all()
            projects = cycle(Project.objects.all())
            with open(test_todos_file) as f:
                test_todos = json.load(f)
            for index, todo in enumerate(test_todos):
                author = authors[index]
                project = next(projects)
                ToDo(author=author, project=project, **todo).save()
                print(f" -> ToDo \"{todo['text']}\" created")
