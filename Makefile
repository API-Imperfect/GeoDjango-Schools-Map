ifneq (,$(wildcard ./.env))
   include .env
   export
   ENV_FILE_PARAM = --env-file .env
endif

build:
	docker-compose up --build --remove-orphans

up:
	docker-compose up

down:
	docker-compose down

migrate:
	docker-compose exec school-api python3 manage.py migrate --noinput

makemigrations:
	docker-compose exec school-api python3 manage.py makemigrations

superuser:
	docker-compose exec school-api python3 manage.py createsuperuser

down-v:
	docker-compose down -v

volume:
	docker volume inspect schools-src_postgres_data


