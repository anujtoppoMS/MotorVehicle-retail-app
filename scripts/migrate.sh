#!/bin/bash

SUPERUSER_EMAIL_PATH="/mnt/secrets-store/DJANGO-SUPERUSER-EMAIL"
SUPER_USER_PATH="/mnt/secrets-store/DJANGO-SUPERUSER-USERNAME"

SUPERUSER_EMAIL=$(cat "$SUPERUSER_EMAIL_PATH" || echo "abc@django.com")
SUPER_USER=$(cat "$SUPER_USER_PATH" || echo "anuj")

# SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"abc@django.com"}
# SUPER_USER=${DJANGO_SUPERUSER_USERNAME:-"anuj"}
cd /BillingSystem
# /opt/bin/python manage.py collectstatic --noinput
/opt/bin/python manage.py migrate --noinput
# /opt/bin/python manage.py createsuperuser --username $SUPER_USER --email $SUPERUSER_EMAIL --noinput || true

# Assign your superuser details to variables

# Check if the superuser already exists
if /opt/bin/python manage.py shell -c "from django.contrib.auth import get_user_model; User = get_user_model(); exit(User.objects.filter(username='$SUPER_USER').exists())"; then
    echo "Superuser with username '$SUPER_USER' already exists. Skipping creation."
else
    /opt/bin/python manage.py createsuperuser --username $SUPER_USER --email $SUPERUSER_EMAIL --noinput
    echo "Superuser '$SUPER_USER' created successfully."
fi