import os
from celery import Celery

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'config.settings.develop')

app = Celery('config')
app.config_from_object('django.cond:settings')
app.autodiscover_tasks()
