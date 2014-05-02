import os

DEBUG = True
ADMINS = ( ('John', 'john@example.com'), 
          ('Mary', 'mary@example.com'),
         )
TEMPLATE_DEBUG = DEBUG
MANAGERS = ADMINS

PROJECT_PATH =  os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  os.path.join(PROJECT_PATH,'../sqlite3.db'),
    }
}

ALLOWED_HOSTS = ['127.0.0.1','0.0.0.0','*']

TIME_ZONE = 'Asia/Shanghai'

LANGUAGE_CODE = 'zh-cn'

SITE_ID = 1

kUSE_I18N = True

USE_L10N = True

USE_TZ = True

MEDIA_ROOT = 'D://www/media/'
MEDIA_URL = '/media/'

STATIC_ROOT = '/var/www/computing-works.com/static/'
STATIC_URL = '/static/'

STATICFILES_DIRS = (
                    "/home/html/static",
)

STATICFILES_FINDERS = (
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
)

SECRET_KEY = 'haha#hehe'

TEMPLATE_LOADERS = (
    'django.template.loaders.filesystem.Loader',
    'django.template.loaders.app_directories.Loader',
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
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.sites',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.admin',
    'register',
    'bootstrap_toolkit',
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

SEND_EMAIL = False

CAPTCHA = {
    'fgcolor': '#254b6f',
    'imagesize': (200, 50),
}

MEDIA_DEBUG_ROOT = 'D://www/media/'