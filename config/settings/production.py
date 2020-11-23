# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/2.2/howto/deployment/checklist/

from .base import *
DEBUG = False

SECRET_KEY = '1tv^5t_81mo3#b%=)+c_07gvt1_c1io0(yto%t$s=9s#!z-asd'

ALLOWED_HOSTS = [
    '',  # LOCALE
    '31.31.196.51',  # REG RU
    '192.168.31.23',
    '127.0.0.1',
    'localhost',
    'prodlogistica.ru',
]

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'prodlogistica',
        'USER': 'dbms',
        'PASSWORD': 'prodlog_t!()N20ms',
        'HOST': 'localhost',
        'PORT': 5432
    },
}
