from pathlib import Path

import dj_database_url as db_url
from decouple import config

BASE_DIR = Path(__file__).resolve().parent.parent

SECRET_KEY = 'test_secret_key'

ALLOWED_HOSTS = ['localhost']

INSTALLED_APPS = [
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',  # Needed for django.contrib.auth
    'django.contrib.staticfiles',  # Needed for DRF browsable API
    'rest_framework',
    'dndtoolshelper.api',
    'tests',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'corsheaders.middleware.CorsMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

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
    'default': db_url.parse(config('DATABASE_URL')),
}

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
    'TEST_REQUEST_DEFAULT_FORMAT': 'json',
}

TIME_ZONE = 'UTC'
USE_TZ = True

STATIC_URL = 'static/'  # https://docs.djangoproject.com/en/3.2/howto/static-files/

CELERY_BROKER_URL = 'memory://'
CELERY_ACCEPT_CONTENT = ['json', 'pickle']
CELERY_TASK_SERIALIZER = 'pickle'
CELERY_RESULT_SERIALIZER = 'pickle'
CELERY_WORKER_PREFETCH_MULTIPLIER = 1
