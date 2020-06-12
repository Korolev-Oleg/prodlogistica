from .base import *

DEBUG = False

SECRET_KEY = '1tv^5t_81mo3#b%=)+c_07gvt1_c1io0(yto%t$s=9s#!z-asd'

ALLOWED_HOSTS = [
    '127.0.0.1',
]

DATABASES = {
    'default': {
        'CONN_MAX_AGE': 0,
        'ENGINE': 'django.db.backends.sqlite3',
        'HOST': 'localhost',
        'NAME': 'project.db',
        'PASSWORD': '',
        'PORT': '',
        'USER': ''
    },
}
