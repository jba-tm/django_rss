#!/usr/bin/env bash
IFS=
DJANGO_SECRET_KEY=$(python3 -c 'import random; print("".join(random.SystemRandom().choice("abcdefghijklmnopqrstuvwxyz0123456789!@#$%^&*(-_=+)") for _ in range(50)))')


DJANGO_SECRET_KEY=$DJANGO_SECRET_KEY \
docker-compose --env-file ./config/.env.dev up --detach --build


sudo docker exec -u root -d django_rss_gunicorn_1 ./venv/bin/python3 manage.py makemigrations
sudo docker exec -u root -d django_rss_gunicorn_1 ./venv/bin/python3 manage.py migrate
sudo docker exec -u root -d django_rss_gunicorn_1 ./venv/bin/python3 manage.py loaddata data
sudo docker exec -u root -d django_rss_gunicorn_1 ./venv/bin/python3 manage.py collectstatic