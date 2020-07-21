install:
	pipenv install

build:
	docker-compose build

run:
	docker-compose up 

stop:
	docker-compose stop 

destroy:
	docker-compose down 

makemigrations:
	docker-compose run web alembic revision --autogenerate

migrate:
	docker-compose run web alembic upgrade head

shell:
	docker-compose run web bash 

python:
	docker-compose run web ipython
