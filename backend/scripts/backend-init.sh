#!/bin/sh

set -e

poetry run ./manage.py collectstatic --noinput
poetry run ./manage.py flush --no-input
poetry run ./manage.py makemigrations
poetry run ./manage.py migrate
poetry run ./manage.py make_users_and_groups
poetry run ./manage.py loaddata project.json todo.json

exec "$@"
