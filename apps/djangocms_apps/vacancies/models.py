from django.db import models
from cms.models.pluginmodel import CMSPlugin


class Vacancies(models.Model):
    """ Vacancies from HeadHunter """
    title = models.CharField(max_length=70, verbose_name='Заголовок')
    description = models.CharField(max_length=63, verbose_name='Описание')
    published = models.DateTimeField(verbose_name='Дата публикации')
    url = models.URLField(verbose_name='Ссылка')

    def __str__(self):
        return self.title

    def normalize(self):
        """TODO This method use only with sqlite -> task.py"""
        self.title = self.title[0:70]
        self.description = self.description[0:63]

    def is_contained(self) -> bool:
        """ Checking for a similar vacancy """
        for vacancy_in_db in Vacancies.objects.all():
            if self.title == vacancy_in_db.title:
                if self.description == vacancy_in_db.description:
                    return True
        return False

    class Meta:
        verbose_name_plural = 'Вакансии'
        verbose_name = 'Вакансия'
        ordering = ['-published']
