import os
from pathlib import Path
from urllib.parse import quote_plus

import dj_database_url

from core.config import conf
from core.utils.settings import getenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = getenv(
    "SECRET_KEY", "django-insecure-a!$qs$%r&5qes6vj!3dkk*74aqr$r$28l0uu)+@0v)#r+h*#_x"
)

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = conf.ALLOWED_HOSTS if conf.ALLOWED_HOSTS else ["*"]
CSRF_TRUSTED_ORIGINS = conf.CSRF_TRUSTED_ORIGINS

# Application definition
INSTALLED_APPS = [
    "django.contrib.admin",
    "django.contrib.auth",
    "django.contrib.contenttypes",
    "django.contrib.sessions",
    "django.contrib.messages",
    "django.contrib.staticfiles",
    "django.contrib.postgres",
    "apps.api",
]

MIDDLEWARE = [
    "django.middleware.security.SecurityMiddleware",
    "whitenoise.middleware.WhiteNoiseMiddleware",
    "django.contrib.sessions.middleware.SessionMiddleware",
    "django.middleware.common.CommonMiddleware",
    "django.middleware.csrf.CsrfViewMiddleware",
    "django.contrib.auth.middleware.AuthenticationMiddleware",
    "django.contrib.messages.middleware.MessageMiddleware",
    "django.middleware.clickjacking.XFrameOptionsMiddleware",
]

ROOT_URLCONF = "core.urls"

TEMPLATES = [
    {
        "BACKEND": "django.template.backends.django.DjangoTemplates",
        "DIRS": [
            os.path.join(BASE_DIR, "templates"),
        ],
        "APP_DIRS": True,
        "OPTIONS": {
            "context_processors": [
                "django.template.context_processors.debug",
                "django.template.context_processors.request",
                "django.contrib.auth.context_processors.auth",
                "django.contrib.messages.context_processors.messages",
            ],
        },
    },
]

WSGI_APPLICATION = "core.wsgi.application"


# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

# Database configuration
# Example: DATABASE_URL = "postgres://user:password@localhost:5432/dbname"
DATABASE_URL = getenv("DATABASE_URL", None)

if DATABASE_URL:
    DATABASES = {
        "default": dj_database_url.parse(DATABASE_URL)
    }
else:
    DATABASES = {
        "default": {
            "ENGINE": "django.db.backends.sqlite3",
            "NAME": BASE_DIR / "db.sqlite3",
        }
    }
# Password validation
# https://docs.djangoproject.com/en/4.1/ref/settings/#auth-password-validators
AUTH_PASSWORD_VALIDATORS = [
    {
        "NAME": "django.contrib.auth.password_validation.UserAttributeSimilarityValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.MinimumLengthValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.CommonPasswordValidator",
    },
    {
        "NAME": "django.contrib.auth.password_validation.NumericPasswordValidator",
    },
]

# DATABASE_ROUTERS = []  # Add your database routers here if needed

# Internationalization
# https://docs.djangoproject.com/en/4.1/topics/i18n/

LANGUAGE_CODE = "en-us"

TIME_ZONE = "UTC"

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/4.1/howto/static-files/

STATIC_URL = getenv("STATIC_URL", "/static/")
STATIC_ROOT = BASE_DIR.parent / "staticfiles"

# WhiteNoise configuration for serving static files
STATICFILES_STORAGE = "whitenoise.storage.CompressedManifestStaticFilesStorage"

MEDIA_URL = getenv("MEDIA_URL", "/media/")
MEDIA_ROOT = "mediafiles"

# Default primary key field type
# https://docs.djangoproject.com/en/4.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = "django.db.models.BigAutoField"
GRAPHQL_CONNECTION_MAX_RESULTS = conf.GRAPHQL_CONNECTION_MAX_RESULTS

# Logging
LOGGING = {
    "version": 1,
    "disable_existing_loggers": False,
    "formatters": {
        "default": {
            "format": "%(asctime)s %(levelname)-8s %(name)-15s %(message)s",
            "datefmt": "%Y-%m-%d %H:%M:%S",
        }
    },
    "handlers": {
        "console": {
            "class": "logging.StreamHandler",
            "level": "DEBUG",
            "formatter": "default",
            "stream": "ext://sys.stdout",
        }
    },
    "loggers": {
        "": {
            "handlers": ["console"],
            "level": "DEBUG",
            "propagate": False,
        },
    },
}

ENVIRONMENT = getenv("ENVIRONMENT", "dev")
APPLICATION_VERSION = getenv("APPLICATION_VERSION", "dev")
APPLICATION_NAME = getenv("APPLICATION_NAME", "django-graphql-federation")
APPLICATION_NAMESPACE = getenv("APPLICATION_NAMESPACE")

FLUENT_HOST = getenv("FLUENT_HOST", None)
FLUENT_PORT = int(getenv("FLUENT_PORT", 24224))

if FLUENT_HOST and FLUENT_PORT:

    def msgpack_default_encode(obj):
        if isinstance(obj, Exception):
            if hasattr(obj, "message"):
                return obj.message
            else:
                return str(obj)
        return obj

    LOGGING = {
        "version": 1,
        "disable_existing_loggers": False,
        "formatters": {
            "default": {
                "format": "%(asctime)s %(levelname)-8s %(name)-15s %(message)s",
                "datefmt": "%Y-%m-%d %H:%M:%S",
            },
            "fluent_formatter": {
                "()": "fluent.handler.FluentRecordFormatter",
                "format": {
                    "level": "%(levelname)s",
                    "hostname": "%(hostname)s",
                    "location": "%(module)s.%(funcName)s",
                    "exception": "%(exc_info)s",
                    "pathname": "%(pathname)s",
                    "filename": "%(filename)s",
                    "threadname": "%(threadName)s",
                    "environment": ENVIRONMENT,
                    "application_version": APPLICATION_VERSION,
                    "application_name": APPLICATION_NAME,
                    "application_namespace": APPLICATION_NAMESPACE,
                },
            },
        },
        "handlers": {
            "console": {
                "class": "logging.StreamHandler",
                "level": "DEBUG",
                "formatter": "default",
                "stream": "ext://sys.stdout",
            },
            "fluent": {
                "level": "DEBUG",
                "class": "fluent.handler.FluentHandler",
                "formatter": "fluent_formatter",
                "tag": "python.logging",
                "host": FLUENT_HOST,
                "port": FLUENT_PORT,
                "msgpack_kwargs": {"default": msgpack_default_encode},
            },
        },
        "loggers": {
            "": {
                "handlers": ["fluent", "console"],
                "level": "DEBUG",
                "propagate": False,
            },
        },
    }


# Add your custom environment variables here
# AWS_ACCESS_KEY_ID = getenv("AWS_ACCESS_KEY_ID")
# AWS_SECRET_ACCESS_KEY = getenv("AWS_SECRET_ACCESS_KEY")
# AWS_REGION_NAME = getenv("AWS_REGION_NAME", "us-east-1")
