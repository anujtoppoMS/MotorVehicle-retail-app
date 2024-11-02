#!/bin/bash
# APP_PORT=${PORT:-8000}
# cd /app/
# /opt/venv/bin/gunicorn --worker-tmp-dir /dev/shm  BillingSystem.wsgi:application --bind "0.0.0.0:${APP_PORT}"

set -e

cd /BillingSystem/

python manage.py makemigrations --noinput

python manage.py migrate --noinput

python manage.py collectstatic --noinput

uwsgi --socket :8000 --master --enable-threads --module BillingSystem.wsgi