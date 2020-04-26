from django.db import models
from django.utils.translation import ugettext as _
from cms.models.fields import models as cms_models
from filer.fields import image


# Create your models here.
class Tabs(models.Model):
    name: models.CharField(_('name'), max_length=128)


class Tab(models.model):
    title: models.CharField(_('title'), )
    img: models.ImageField(_('image'), upload_to='')
    header: models.CharField(_('header'), max_length=55)
    content: models.TextField(_('content'))
    points: models.TextField(_('points'))

    about: models.BooleanField(_('about us'))
    contacts: models.BooleanField(_('contacts'))
    map: models.BooleanField(_('map'))
