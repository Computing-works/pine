from __future__ import with_statement
import os

#
# Configuration file must contain:
#
# DEBUG
# DATABASE_ENGINE
# DATABASE_NAME
# DATABASE_USER
# DATABASE_PASSWORD
# DATABASE_HOST
# DATABASE_PORT
# SECRET_KEY
# TIME_ZONE
# LANGUAGE_CODE
# USE_I18N
# EMAIL_HOST
# EMAIL_PORT
# DEFAULT_FROM_EMAIL
# MEDIA_ROOT
# SEND_EMAIL
# ADMINS
#
# See Django documentation for possible values.
#
path = os.path.expanduser(os.path.join(os.path.dirname(__file__), 'conf.py'))

if os.path.exists(path):
    with open(path) as conf:
        exec conf.read()
else:
    raise RuntimeError('configuration not found at %s' % path)

TEMPLATE_DEBUG = DEBUG
MANAGERS = ADMINS

TIME_ZONE = 'Asia/Shanghai'
LANGUAGE_CODE = 'zh-cn'
SITE_ID = 1
kUSE_I18N = True
USE_L10N = True
USE_TZ = True

MEDIA_URL = '/media/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
#	"/var/www/computing-works.com/static/",
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)


TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
)

from django.conf.global_settings import TEMPLATE_CONTEXT_PROCESSORS
TEMPLATE_CONTEXT_PROCESSORS += (
  'django.contrib.auth.context_processors.auth',
  'django.core.context_processors.i18n',
  'django.core.context_processors.request',
  'zinnia.context_processors.version',  # Optional
)

TEMPLATE_DIRS = (
    "/home/html/django_templates",
    os.path.join( PROJECT_PATH, 'templates'),
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'pine.urls'

WSGI_APPLICATION = 'pine.wsgi.application'


INSTALLED_APPS = (
    'django.contrib.auth',
    'django.contrib.admin',
    'django.contrib.sites',
    'django.contrib.comments',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.contenttypes',
    'register',
    'captcha',
    'bootstrap_toolkit',
    'tagging',
    'mptt',
    'zinnia',
    'django-groundwork',
)

SESSION_SERIALIZER = 'django.contrib.sessions.serializers.JSONSerializer'

LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse'
        }
    },
    'handlers': {
        'mail_admins': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'django.utils.log.AdminEmailHandler'
        }
    },
    'loggers': {
        'django.request': {
            'handlers': ['mail_admins'],
            'level': 'ERROR',
            'propagate': True,
        },
    }
}

# Parse database configuration from $DATABASE_URL
# import dj_database_url
# DATABASES['default'] =  dj_database_url.config()

# Honor the 'X-Forwarded-Proto' header for request.is_secure()
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')


LOGIN_URL  = '/account/login/'
LOGIN_REDIRECT_URL = '/'

MIN_PASSWORD_LEN = 6
CHECK_STRENGTH = True

CAPTCHA = {
    'fgcolor': '#254b6f',
    'imagesize': (200, 50),
}



