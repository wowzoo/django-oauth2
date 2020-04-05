#!/bin/bash

# Database migration
python manage.py makemigrations unicorns
python manage.py migrate

# Create superuser
export DJANGO_SUPERUSER_PASSWORD=demo1234!
export DJANGO_SUPERUSER_USERNAME=demo
export DJANGO_SUPERUSER_EMAIL=wowzoo@gmail.com
python manage.py makesuperuser

# Collect static files
mkdir -p static
python manage.py collectstatic

# Start server
gunicorn --worker-class gevent --workers 2 --bind 0.0.0.0:8080 api.wsgi --max-requests 10000 --timeout 5 --keep-alive 5 --log-level info
