#!/bin/bash
APPLICATION_ASGI=core.asgi:application

echo "Running Django App..."
echo "APPLICATION_ASGI: ${APPLICATION_ASGI}"

gunicorn ${APPLICATION_ASGI} --conf gunicorn.conf.py
