#!make

key:
	poetry run python -c "from django.core.management.utils import get_random_secret_key;print(get_random_secret_key())"

db-reset:
	rm -f ./data/db.sqlite3
	rm -f ./userapp/migrations/00*.py
	rm -f ./todoapp/migrations/00*.py
	poetry run ./manage.py makemigrations
	poetry run ./manage.py migrate
	poetry run ./manage.py make_users_and_groups
	poetry run ./manage.py loaddata project.json todo.json

back:
	poetry run ./manage.py runserver 127.0.0.1:8000 --insecure

front:
	cd ./frontend && npm start run

build:
	cd ./frontend && npm run build

reset: db-reset back
