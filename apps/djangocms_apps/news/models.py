from django.db import models
from cms.models.pluginmodel import CMSPlugin


# Create your models here.
class Vacancy(models.Model):
    title = models.CharField(max_length=143, verbose_name='Заголовок')
    date = models.CharField(max_length=13, verbose_name='Дата')
    url = models.URLField(verbose_name='Ссылка')
