PROJECT_NAME=project
MAIN_APP_NAME=app

init:
	poetry init

install:
	poetry install

project:
	poetry run django-admin startproject $(PROJECT_NAME) .

app:
	poetry run ./manage.py startapp $(MAIN_APP_NAME)

migration:
	poetry run ./manage.py makemigrations $(MAIN_APP_NAME)

migrate:
	poetry run ./manage.py migrate

shell:
	poetry run ./manage.py shell

superuser:
	poetry run ./manage.py createsuperuser

run-dev:
	poetry run ./manage.py runserver 8000

notebook:
	poetry run ./manage.py shell_plus --notebook
