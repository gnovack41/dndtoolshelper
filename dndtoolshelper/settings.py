import logging
import os
import ssl
from datetime import datetime, timezone
from functools import partial
from pathlib import Path

import dj_database_url as db_url
from celery.schedules import crontab
from decouple import Csv, config

BASE_DIR = Path(__file__).resolve().parent.parent

DEBUG = config('DEBUG', default=False, cast=bool)

SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='', cast=Csv())

CORS_ALLOWED_ORIGINS = config('CORS_ORIGINS', default='', cast=Csv())
CORS_ALLOWED_ORIGIN_REGEXES = config('CORS_ORIGINS_REGEX', default='', cast=Csv())

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',  # Needed for django.contrib.auth
    'django.contrib.staticfiles',  # Needed for DRF browsable API
    'corsheaders',
    'rest_framework',
    'dndtoolshelper.api',
    'dndtoolshelper.dndbeyond',
    'graphene_django',
    'django_filters',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

SECURE_HSTS_SECONDS = 60 * 60 * 24 * 365

ROOT_URLCONF = 'dndtoolshelper.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
            ],
        },
    },
]

WSGI_APPLICATION = 'dndtoolshelper.wsgi.application'

DATABASES = {
    'default': db_url.parse(config('DATABASE_URL'))
}

# HEROKU-SPECIFIC: free and premium Redis addons use different env vars
REDIS_URL = os.environ.get('REDIS_TLS_URL', config('REDIS_URL'))

REST_FRAMEWORK = {
    'DEFAULT_METADATA_CLASS': None,
    'DEFAULT_RENDERER_CLASSES': [
        'rest_framework.renderers.JSONRenderer',
    ],
    'DEFAULT_PARSER_CLASSES': [
        'rest_framework.parsers.JSONParser',
    ],
    'DEFAULT_AUTHENTICATION_CLASSES': [],
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.AllowAny',
    ],
}

if DEBUG:
    # Only enable the browsable API in DEBUG mode
    REST_FRAMEWORK['DEFAULT_RENDERER_CLASSES'].append('rest_framework.renderers.BrowsableAPIRenderer')

logging.captureWarnings(True)
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'handlers': {
        'console': {
            'class': 'logging.StreamHandler',
        },
    },
    'loggers': {
        'dndtoolshelper': {
            'level': config('LOG_LEVEL', 'DEBUG' if DEBUG else 'INFO'),
            'handlers': ['console'],
        },
        'py.warnings': {
            'handlers': ['console'],
        },
    },
}

TIME_ZONE = 'UTC'
USE_TZ = True

STATIC_URL = 'static/'  # https://docs.djangoproject.com/en/3.2/howto/static-files/

CELERY_BROKER_URL = REDIS_URL
CELERY_ACCEPT_CONTENT = ['json', 'pickle']
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_WORKER_PREFETCH_MULTIPLIER = 1

if not DEBUG:
    # HEROKU-SPECIFIC: Allow self-signed certs
    CELERY_BROKER_USE_SSL = {'ssl_cert_reqs': ssl.CERT_NONE}

CELERY_BEAT_SCHEDULE = {
    'sync_items_with_5etools_daily': {
        'task': 'dndtoolshelper.api.tasks.sync_dndtools_items.sync_dndtools_items',
        'schedule': crontab(minute=0, hour=2, nowfun=partial(datetime.now, tz=timezone.utc)),
    }
}

GRAPHENE = {
    'SCHEMA': 'dndtoolshelper.api.schema.schema',
}

REQUESTS_TIMEOUT = config('REQUESTS_TIMEOUT', default=10.0, cast=float)

DND_API_URL = config('DND_API_URL')
DND_BEYOND_URL = config('DND_BEYOND_URL')
