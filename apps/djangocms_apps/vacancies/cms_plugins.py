from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .models import Vacancies
from .task import update_vacancies


@plugin_pool.register_plugin
class VacancyPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "vacancy.html"
    name = 'Блок вакансий'
    cache = False

    def render(self, context, instance, placeholder):
        update_vacancies.delay()  # launching a celery task that updates the news
        context.update(
            {
                'instance': instance,
                'vacancy': Vacancies.objects.all()
            }
        )
        return context
