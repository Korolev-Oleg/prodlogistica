from cms.plugin_base import CMSPluginBase
from cms.plugin_pool import plugin_pool
from cms.models.pluginmodel import CMSPlugin
from django.utils.translation import ugettext_lazy as _

from .models import Contacts


@plugin_pool.register_plugin
class Phone(CMSPluginBase):
    model = CMSPlugin
    render_template = 'phone.html'
    name = 'Телефон компании'
    cache = False

    def render(self, context, instance, placeholder):
        if len(Contacts.objects.all()) > 0:
            context.update(
                {
                    'instance': instance,
                    'phone': Contacts.objects.all()[0].phone
                }
            )
            return context


@plugin_pool.register_plugin
class Email(CMSPluginBase):
    model = CMSPlugin
    render_template = 'email.html'
    name = 'Почта компании'
    cache = False

    def render(self, context, instance, placeholder):
        if len(Contacts.objects.all()) > 0:
            context.update(
                {
                    'instance': instance,
                    'email': Contacts.objects.all()[0].email
                }
            )
            return context


@plugin_pool.register_plugin
class Address(CMSPluginBase):
    model = CMSPlugin
    render_template = 'address.html'
    name = 'Адресс компании'
    cache = False

    def render(self, context, instance, placeholder):
        if len(Contacts.objects.all()) > 0:
            context.update(
                {
                    'instance': instance,
                    'address': Contacts.objects.all()[0].address
                }
            )
            return context
