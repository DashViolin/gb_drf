import json
import os

from django.conf import settings
from django.contrib.auth import get_user_model
from django.core.management.base import BaseCommand
from dotenv import load_dotenv

COLOR_GREEN = "\033[1;32m"
COLOR_OFF = "\033[0m"


class Command(BaseCommand):
    help = "Use this command to create admin and some test users"

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

        test_users_file = settings.DATA_DIR / "test_data" / "test_users.json"
        if test_users_file.exists:
            with open(test_users_file) as f:
                test_users = json.load(f)
            for user in test_users:
                user_model.objects.create_user(**user)
                print(f" -> User \"{COLOR_GREEN}{user['username']}{COLOR_OFF}\" created")
