import os
from os.path import abspath, dirname, join

from django.core.exceptions import ImproperlyConfigured


def get_env_variable(var_name):
    """ Get the environment variable or return exception """
    try:
        return os.environ[var_name]
    except KeyError:
        error_msg = "Set the %s environment variable" % var_name
        raise ImproperlyConfigured(error_msg)

# PATH CONFIGURATION
here = lambda *x: join(abspath(dirname(__file__)), *x)
PROJECT_ROOT = here("..", "..")
root = lambda *x: join(abspath(PROJECT_ROOT), *x)

# MANAGER CONFIGURATION
ADMINS = (
    ('Alexander Nelzin', 'asnelzin@gmail.com'),
)

MANAGERS = ADMINS

# GENERAL CONFIGURATION
TIME_ZONE = 'UTC'
DEFAULT_CHARSET = 'utf-8'
LANGUAGE_CODE = 'ru'

SITE_ID = 1

USE_I18N = False
USE_L10N = True

# MEDIA
MEDIA_ROOT = root('files/media')
MEDIA_URL = '/media/'
ADMIN_MEDIA_PREFIX = '/admin-media/'

# STATIC FILES
STATIC_URL = '/static/'

STATICFILES_DIRS = (
    root('medis/static'),
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    'django.contrib.staticfiles.finders.FileSystemFinder',
)

# TEMPLATE
TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
    # 'django.template.loaders.eggs.Loader',
)

TEMPLATE_DIRS = (
    root('medis/templates'),
)

TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.media',
    "django.core.context_processors.i18n",
    "django.core.context_processors.static",
    'django.core.context_processors.request',
)

# MIDDLEWARE
MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
)

# APP
INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.staticfiles',

    'medis.apps.stats',
)

# URL
ROOT_URLCONF = 'medis.urls'

# KEY
SECRET_KEY = get_env_variable('SECRET_KEY')
