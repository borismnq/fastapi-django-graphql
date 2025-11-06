#!/bin/bash
APPLICATION_ASGI=core.asgi:fastapp

echo "Running FastAPI App..."
echo "APPLICATION_ASGI: ${APPLICATION_ASGI}"

gunicorn ${APPLICATION_ASGI} --conf gunicorn.conf.py
