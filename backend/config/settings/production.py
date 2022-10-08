from .base import *

DEBUG = False

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
