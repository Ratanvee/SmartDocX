#!/bin/sh
apt-get update && apt-get install -y ghostscript
python manage.py migrate
python manage.py collectstatic --noinput
gunicorn app.wsgi:application --bind 0.0.0.0:8000
