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

# from django.utils.functional import curry
from django.views.defaults import (server_error, page_not_found,
                                   permission_denied)
from django.views.static import serve

from apps.robots.views import robots
from apps.protected_static.views import protected_static

admin.autodiscover()

# TODO enable errors handling on this line
# ERRORS HANDLING
# handler400 = curry(
#     page_not_found,
#     exception=Exception('Page not Found'),
#     template_name='errs/400.html'
# )
#
# handler403 = curry(
#     permission_denied,
#     exception=Exception('Permission Denied'),
#     template_name='errs/403.html'
# )
#
# handler404 = curry(
#     page_not_found,
#     exception=Exception('Page not Found'),
#     template_name='errs/404.html'
# )
#
# handler500 = curry(
#     server_error,
#     exception=Exception('Page not Found'),
#     template_name='errs/500.html'
# )

urlpatterns = [
    url(r'^sitemap\.xml/$', sitemap, {'sitemaps': {'cmspages': CMSSitemap}}),
    url(r'^robots.txt/$', robots),
<<<<<<< HEAD
<<<<<<< HEAD


    url(r'^media/(?P<path>.*)$', serve,
        {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
=======
    url(r'^ru/static/', protected_static, name="protected_static"),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
>>>>>>> 32ef66c86bb108fdaead994d7e0d492837b7805b
=======
    url(r'^ru/static/', protected_static, name="protected_static"),
    url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT, 'show_indexes': True}),
>>>>>>> 32ef66c86bb108fdaead994d7e0d492837b7805b
    url(r'', include('django.contrib.staticfiles.urls')),
    # url(r'^404$', handler404),
]

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
