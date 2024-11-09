#!/bin/bash
# APP_PORT=${PORT:-8000}
# cd /app/
# /opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm  BillingSystem.wsgi:application --bind "0.0.0.0:${APP_PORT}"

set -e

SUPER_USER=${DJANGO_SUPERUSER_USERNAME:-"anuj"}
SUP_PASS=${DJANGO_SUPERUSER_PASSWORD:-"anuj@1992"}
SUP_EMAIL=${DJANGO_SUERPUSER_EMAIL:-"mailme@anujtoppo.com"}

cd /BillingSystem/

python manage.py makemigrations --noinput

python manage.py migrate --noinput

python manage.py createsuperuser --username $SUPER_USER --email $SUP_EMAIL --noinput || true

python manage.py collectstatic --noinput

uwsgi --socket :8000 --master --enable-threads --module BillingSystem.wsgi