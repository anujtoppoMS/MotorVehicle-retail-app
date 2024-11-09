#!/bin/bash

# SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"abc@django.com"}
# cd /app/

# /opt/venv/bin/python manage.py migrate --noinput
# /opt/venv/bin/python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"abc@django.com"}

cd /BillingSystem/

python manage.py migrate --noinput
python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true
