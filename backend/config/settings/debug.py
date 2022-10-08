from .base import *

DEBUG = True

INTERNAL_IPS = os.environ.get("DJANGO_DEBUG_INTERNAL_IPS").split()

CORS_ALLOWED_ORIGINS = [
    "http://localhost:3000",
    "http://127.0.0.1:3000",
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': DATA_DIR / 'db.sqlite3',
    }
}
