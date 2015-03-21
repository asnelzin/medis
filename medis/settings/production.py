# settings/production.py
from .base import *

# DEBUG
DEBUG = False
TEMPLATE_DEBUG = DEBUG
SESSION_SAVE_EVERY_REQUEST = False

ALLOWED_HOSTS = ['*']

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'HOST': 'localhost',
        'NAME': 'db',
        'USER': 'postgres',
        'PASSWORD': get_env_variable('POSTGRES_PASSWORD'),
    }
}

# STATIC
STATIC_ROOT = root('files/static')
