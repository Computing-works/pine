import os

DEBUG = True

ADMINS = ( ('John', 'john@example.com'), 
          ('Mary', 'mary@example.com'),
         )

ALLOWED_HOSTS = ['127.0.0.1','0.0.0.0','*']

PROJECT_PATH =  os.path.dirname(os.path.abspath(__file__))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME':  os.path.join(PROJECT_PATH,'../sqlite3.db'),
    }
}

MEDIA_ROOT = 'D://www/media/'
STATIC_ROOT = 'D://www/static/'

SEND_EMAIL = False

SECRET_KEY = 'haha#hehe'