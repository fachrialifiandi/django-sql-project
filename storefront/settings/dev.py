from .common import *

DEBUG = True

SECRET_KEY = 'django-insecure-d5n^$^snsowl#=+#+=u34*6mqh@+anixwqz=76ca4ed3j7=vow'

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'storefront',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': '#Fachri2006',
        'CONN_MAX_AGE': 60,
    }
}