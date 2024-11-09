#!/bin/bash

# SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"abc@django.com"}
# cd /app/

# /opt/venv/bin/python manage.py migrate --noinput
# /opt/venv/bin/python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true

SUPER_USER=${DJANGO_SUPERUSER_USERNAME:-"anuj"}
SUP_PASS=${DJANGO_SUPERUSER_PASSWORD:-"anuj@06031992"}
SUP_EMAIL=${DJANGO_SUERPUSER_EMAIL:-"mailme@anujtoppo.com"}

cd /BillingSystem/

python manage.py migrate --noinput
python manage.py createsuperuser --username $SUPER_USER --password $SUP_PASS  --email $SUP_EMAIL --noinput || true