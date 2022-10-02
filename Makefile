#!make

include ./backend/config/.env
export

WORK_DIR=$(shell pwd)
DOCKER_USER=$(shell whoami)


key:
	poetry run python -c "from django.core.management.utils import get_random_secret_key;print(get_random_secret_key())"

install:
	sudo apt update && sudo apt upgrade -y
	sudo apt install python-is-python3 -y
	sudo apt install python3-pip python3-cachecontrol -y 
	sudo apt install docker.io docker-compose nodejs npm -y
	sudo python3 -m pip install --upgrade pip
	sudo pip3 install poetry
	sudo usermod -aG docker ${DOCKER_USER}
	sudo systemctl enable docker && sudo systemctl restart docker
	sudo reboot

init:
	cd ./backend && poetry install

db-purge:
	rm -f ./backend/data/db.sqlite3
	rm -f ./backend/userapp/migrations/00*.py
	rm -f ./backend/todoapp/migrations/00*.py
	sudo rm -rf ./backend/data/pg_data/
	mkdir ./backend/data/pg_data/ -p

db-init:
	mkdir ./backend/data/pg_data/ -p
	cd ./backend && poetry run ./manage.py makemigrations
	cd ./backend && poetry run ./manage.py migrate
	cd ./backend && poetry run ./manage.py make_users_and_groups
	cd ./backend && poetry run ./manage.py loaddata project.json todo.json

db-reset: db-purge db-init

back-run:
	cd ./backend && poetry run ./manage.py runserver 127.0.0.1:8000 --insecure

front-run:
	cd ./frontend && npm start run

front-build:
	cd ./frontend && npm run build

back-reset: db-reset back-run


dc-build:
	docker-compose up --build --remove-orphans

dc-up:
	docker-compose up -d

dc-up-verb:
	docker-compose up

dc-down:
	sudo aa-remove-unknown  # fix-docker-permission-denied
	docker-compose down --remove-orphans


up: db-purge dc-up

dc-reset: down up


build: dc-down db-purge front-build dc-build dc-up

build-verb: dc-down db-purge front-build dc-build dc-up-verb
