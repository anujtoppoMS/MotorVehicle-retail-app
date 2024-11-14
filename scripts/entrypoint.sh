#!/bin/bash
set -e

/opt/bin/python manage.py migrate

# uwsgi --socket :8000 --master --enable-threads --module BillingSystem.wsgi:application
uwsgi --socket :8020 --master --enable-threads --buffer-size 32768 --module BillingSystem.wsgi:application