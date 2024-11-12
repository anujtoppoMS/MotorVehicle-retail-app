#!/bin/bash
# APP_PORT=${PORT:-8000}
# cd /app/
# /opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm  BillingSystem.wsgi:application --bind "0.0.0.0:${APP_PORT}"
# SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"abc@django.com"}
# SUPER_USER=${DJANGO_SUPERUSER_USERNAME:-"anuj"}

set -e

# /opt/bin/python manage.py wait_for_db
# /opt/bin/python manage.py collectstatic --noinput
/opt/bin/python manage.py migrate
# /opt/bin/python manage.py createsuperuser --username $SUPER_USER --email $SUPERUSER_EMAIL --noinput || true

uwsgi --socket :8080 --master --enable-threads --module BillingSystem.wsgi
