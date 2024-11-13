#!/bin/bash

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"abc@django.com"}
SUPER_USER=${DJANGO_SUPERUSER_USERNAME:-"anuj"}

/opt/bin/python manage.py collectstatic --noinput
/opt/bin/python manage.py migrate --noinput
/opt/bin/python manage.py createsuperuser --username $SUPER_USER --email $SUPERUSER_EMAIL --noinput || true
