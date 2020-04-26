#!/bin/bash

# Database migration
python manage.py makemigrations
python manage.py migrate

# Create superuser
# below variables are defined in Dockerfile
# DJANGO_SUPERUSER_PASSWORD, DJANGO_SUPERUSER_USERNAME, DJANGO_SUPERUSER_EMAIL
python manage.py makesuperuser

# Collect static files
python manage.py collectstatic

# Start server
# $EXPOSED_PORT is defined in Dockerfile
gunicorn --worker-class gevent \
         --workers 2 \
         --bind 0.0.0.0:"$EXPOSED_PORT" \
         --max-requests 10000 \
         --timeout 5 \
         --keep-alive 5 \
         --log-level info \
         api.wsgi
