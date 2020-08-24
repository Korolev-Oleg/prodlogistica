from django.db import models


# Create your models here.
class Contacts(models.Model):
    address = models.CharField(max_length=256, verbose_name='Адрес компании')
    phone = models.CharField(max_length=100, verbose_name='Телефон')
    email = models.EmailField(verbose_name='Почта')

    class Meta:
        verbose_name_plural = 'Контакты'
        verbose_name = 'Контакт'

    def __str__(self):
        return "Редактировать контакты компании"
