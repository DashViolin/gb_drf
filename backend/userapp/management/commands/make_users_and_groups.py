import json
import os

from django.conf import settings
from django.contrib.auth import get_user_model
from django.contrib.auth.models import Group, Permission
from django.core.management.base import BaseCommand
from dotenv import load_dotenv

from todoapp.models import Project, ToDo
from userapp.models import CustomUser

COLOR_GREEN = "\033[1;32m"
COLOR_OFF = "\033[0m"

GROUPS_PERMISSIONS = {
    "Developers": {
        CustomUser: ["view"],
        Project: ["view"],
        ToDo: ["add", "change", "delete", "view"],
    },
    "Project owners": {
        CustomUser: ["view"],
        Project: ["add", "change", "delete", "view"],
        ToDo: ["add", "change", "delete", "view"],
    },
}
USER_GROUP_MAPPING = {"Developers": ["user1", "user2"], "Project owners": ["user3"]}


class Command(BaseCommand):
    help = "Use this command to create admin, some test users and groups with permissions"

    def create_groups(self):
        for group_name in GROUPS_PERMISSIONS:
            group, created = Group.objects.get_or_create(name=group_name)
            for model_cls in GROUPS_PERMISSIONS[group_name]:
                for perm_name in GROUPS_PERMISSIONS[group_name][model_cls]:
                    codename = f"{perm_name}_{model_cls._meta.model_name}"
                    try:
                        perm = Permission.objects.get(codename=codename)
                        group.permissions.add(perm)
                        self.stdout.write(f"Adding {codename} to group {group}")
                    except Permission.DoesNotExist:
                        self.stdout.write(f"{codename} not found")

    def handle(self, *args, **options):
        if settings.ENV_PATH.exists:
            load_dotenv(settings.ENV_PATH)
        else:
            FileExistsError(f"Can't find {settings.ENV_PATH} file with environment variables")

        print(f"{COLOR_GREEN}--> Create users <--{COLOR_OFF}")
        user_model = get_user_model()

        su_name = os.environ.get("DJANGO_SUPERUSER_USERNAME")
        su_passwd = os.environ.get("DJANGO_SUPERUSER_PASSWORD")
        su_email = os.environ.get("DJANGO_SUPERUSER_EMAIL")
        if all([su_name, su_passwd, su_email]):
            user_model.objects.create_superuser(
                username=su_name,
                password=su_passwd,
                email=su_email,
                first_name="su",
                last_name="su",
            )
            print(f' -> Superuser "{COLOR_GREEN}{su_name}{COLOR_OFF}" created')

        self.create_groups()

        test_users_file = settings.DATA_DIR / "test_data" / "test_users.json"
        if test_users_file.exists:
            with open(test_users_file) as f:
                test_users = json.load(f)
            for user in test_users:
                user_model.objects.create_user(**user)
                for group_name in USER_GROUP_MAPPING:
                    group = Group.objects.get(name=group_name)
                    current_user_model = CustomUser.objects.get(username=user["username"])
                    if user["username"] in USER_GROUP_MAPPING[group_name]:
                        current_user_model.groups.add(group)
                print(f" -> User \"{COLOR_GREEN}{user['username']}{COLOR_OFF}\" created")
