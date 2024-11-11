#!/bin/bash

# SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"abc@django.com"}
# cd /app/

# /opt/venv/bin/python manage.py migrate --noinput
# /opt/venv/bin/python manage.py createsuperuser --email $SUPERUSER_EMAIL --noinput || true

SUPERUSER_EMAIL=${DJANGO_SUPERUSER_EMAIL:-"abc@django.com"}
SUPER_USER=${DJANGO_SUPERUSER_USERNAME:-"anuj"}

# cd /BillingSystem/

/opt/bin/python manage.py collectstatic --noinput
/opt/bin/python manage.py migrate --noinput
/opt/bin/python manage.py createsuperuser --username $SUPER_USER --email $SUPERUSER_EMAIL --noinput || true

# USER_EXISTS=$(echo "from django.contrib.auth import get_user_model; User = get_user_model(); print(User.objects.filter(username='$SUPER_USER').exists())" | /opt/bin/python manage.py shell)
# if [ -z "$USER_EXISTS" ]; then
#     /opt/bin/python manage.py createsuperuser --username $SUPER_USER --email $SUPERUSER_EMAIL --noinput
# else
#      echo "User $SUPER_USER already exists"
# fi