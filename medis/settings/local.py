# settings/local.py
from .base import *

# DEBUG
DEBUG = True
TEMPLATE_DEBUG = DEBUG
SESSION_SAVE_EVERY_REQUEST = True

ALLOWED_HOSTS = []

# DATABASE
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': 'db.sqlite3',
    }
}

# TEMPLATE
TEMPLATE_CONTEXT_PROCESSORS += ('django.core.context_processors.debug',)
