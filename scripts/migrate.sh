#!/bin/bash

# SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"abc@django.com"}
# cd /app/

# /opt/venv/bin/python manage.py migrate --noinput
# /opt/venv/bin/python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"abc@django.com"}
SUPER_USER=${DJANGO_SUPERUSER_USERNAME:-"anuj"}

cd /BillingSystem/

python manage.py migrate --noinput
python manage.py createsuperuser --username $SUPER_USER --email $SUPERUSER_EMAIL --noinput || true
