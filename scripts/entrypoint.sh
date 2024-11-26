#!/bin/bash
set -e
# APP_PORT=${PORT:-8000}
cd 
/opt/bin/python manage.py migrate --noinput
# uwsgi --socket :8000 --master --enable-threads --module BillingSystem.wsgi:application
# /opt/bin/uwsgi --http :8000 --master --enable-threads --buffer-size 32768 --module BillingSystem.wsgi:application
# /opt/bin/gunicorn --worker-tmp-dir /dev/shm BillingSystem.wsgi:application --timeout 120 --log-level=debug --bind "0.0.0.0:${APP_PORT}"

# Ensure only one instance of uWSGI is started 
if [ ! -f /tmp/uwsgi.pid ]; then
    /opt/bin/uwsgi --ini uwsgi.ini
fi
exec "$@"