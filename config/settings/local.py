from .base import *


DEBUG = config('DEBUG', default=False, cast=bool)

ALLOWED_HOSTS = ['*']

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': config('NAMEDB'),
        'USER': config('USERDB'),
        'PASSWORD': config('PASSWORDDB'),
        'HOST': 'localhost',
        'PORT': ''
       },
   }
