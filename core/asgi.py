"""
ASGI config for core project.

It exposes the ASGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/4.1/howto/deployment/asgi/
"""
import os

from django.core.asgi import get_asgi_application
from prometheus_fastapi_instrumentator import Instrumentator

os.environ.setdefault("DJANGO_SETTINGS_MODULE", "core.settings.base")

application = get_asgi_application()

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.fastapi import GraphQLRouter

from core.schema import schema

# Simple context getter - customize as needed
async def get_context():
    return {}

# GraphQL
graphql_app = GraphQLRouter(schema, path="/", context_getter=get_context)
fastapp = FastAPI(title="Django GraphQL Federation API")

# Prometheus metrics
Instrumentator().instrument(fastapp).expose(fastapp)

# CORS configuration
origins = [
    "http://localhost:8000",
    "http://localhost:3000",
    "https://studio.apollographql.com",
]

fastapp.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Include GraphQL router
fastapp.include_router(graphql_app, prefix="/api/graphql")


@fastapp.get("/api/health/", status_code=200)
def health_check():
    """Health check endpoint"""
    return {"status": "ok", "service": "django-graphql-federation"}


@fastapp.get("/api/info/")
def application_info():
    """Application information endpoint"""
    return {
        "name": "Django GraphQL Federation Template",
        "version": "1.0.0",
        "description": "A template for building GraphQL Federation services with Django, FastAPI, and Strawberry"
    }
