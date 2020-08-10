from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .models import Vacancy
from .task import update_news


@plugin_pool.register_plugin
class NewsPlugin(CMSPluginBase):
    model = CMSPlugin
    render_template = "news_plugin.html"
    name = 'Блок новостей'
    cache = False

    def render(self, context, instance, placeholder):
        update_news.delay()
        context.update(
            {
                'instance': instance,
                'vacancy': Vacancy.objects.all()
            }
        )
        return context
