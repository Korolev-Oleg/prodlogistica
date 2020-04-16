# -*- coding: utf-8 -*-
"""
WSGI config for django_cms project.

It exposes the WSGI callable as a module-level variable named ``application``.

For more information on this file, see
https://docs.djangoproject.com/en/2.2/howto/deployment/wsgi/
"""

import os, sys

if sys.version < "3.7.6":
    os.execle("/var/www/u0721006/data/www/venv/bin/", "python3", *sys.argv)

from django.core.wsgi import get_wsgi_application

sys.path.insert(0, '/var/www/u0721006/data/www/prodlogistica.ru/prodlogistica')
sys.path.insert(1, '/var/www/u0721006/data/www'
                   '/venv/lib/python3.7/site-packages')

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'prodlogistica.settings')

os.execl = "/var/www/u0721006/data/www/venv/bin/"

application = get_wsgi_application()
