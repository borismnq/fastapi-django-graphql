#!/bin/bash
APPLICATION_ASGI=core.asgi:application

echo "Running Django App..."
echo "APPLICATION_ASGI: ${APPLICATION_ASGI}"

# Run database migrations
echo "Running database migrations..."
python manage.py migrate --noinput

# Collect static files
echo "Collecting static files..."
python manage.py collectstatic --noinput

gunicorn ${APPLICATION_ASGI} --conf gunicorn.conf.py
