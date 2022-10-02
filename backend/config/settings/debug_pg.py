from .base import *

DEBUG = True

INTERNAL_IPS = os.environ.get("DJANGO_DEBUG_INTERNAL_IPS").split()

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': os.environ.get("DJANGO_DB_NAME"),
        'USER': os.environ.get("DJANGO_DB_USER"),
        'PASSWORD': os.environ.get("DJANGO_DB_PASSWORD"),
        'HOST': os.environ.get("POSTGRES_HOST"),
        'PORT': '5432',
    }
}
