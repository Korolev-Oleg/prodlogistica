# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from cms.sitemaps import CMSSitemap
from django.conf import settings
from django.conf.urls import url
from django.conf.urls.i18n import i18n_patterns
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.urls import include
from django.utils.functional import curry
from django.views.static import serve
from config.apps.robots.views import robots
from django.views.defaults import (server_error, page_not_found,
                                   permission_denied, bad_request)

admin.autodiscover()


# ERRORS HANDLING
handler404 = curry(page_not_found, exception=Exception('Page not Found'),
                   template_name='errs/404.html')
handler403 = curry(permission_denied, exception=Exception('Permission Denied'),
                   template_name='errs/403.html')
handler500 = curry(server_error, exception=Exception('Page not Found'),
                   template_name='errs/500.html')

urlpatterns = [
    # url(r'^/$', include('config.apps.error_handler.urls')),
    url(r'^sitemap\.xml/$', sitemap,
        {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^robots.txt/$', robots),

    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
    url(r'', include('django.contrib.staticfiles.urls')),

    url(r'^404$', handler404),
]

# errors handling
# urlpatterns += [
#     url(r'^400$', curry(bad_request, template_name='errors/400.html')),
#     url(r'^403$', curry(permission_denied, template_name='errors/403.html')),
#     url(r'^500$', curry(server_error, template_name='errors/500.html')),
# ]

urlpatterns += i18n_patterns(
    url(r'^admin/', admin.site.urls),  # NOQA
    url(r'^', include('cms.urls')),
)

# This is only needed when using runserver.
if settings.DEBUG:
    urlpatterns = [
                      url(r'^media/(?P<path>.*)$', serve,
                          {'document_root': settings.MEDIA_ROOT,
                           'show_indexes': True}),
                  ] + staticfiles_urlpatterns() + urlpatterns
