from django.contrib import admin

from .models import Vacancies


@admin.register(Vacancies)
class VacancyAdmin(admin.ModelAdmin):
    pass
