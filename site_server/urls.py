# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.conf import settings
from django.conf.urls import url
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.sitemaps.views import sitemap
from django.urls import include, re_path
from django.views.static import serve

from allauth import urls as socialmarket
from api.urls import router
from api.views import SocialLoginView, DonateView, VolunteerAjax, ContactAjax, RecordAudioAjax
from cms.sitemaps import CMSSitemap

'''
Main site urls. Here we setup
'''
urlpatterns = [
    # sitemap
    url(r'^sitemap\.xml$', sitemap, {'sitemaps': {'cmspages': CMSSitemap}}),
]

# urlpatterns += i18n_patterns(
urlpatterns += [
       # Social Market accounts management
       url('accounts/', include(socialmarket)),
       url('accounts/social_login', SocialLoginView.as_view()),
       # Seperate API for our content and auth
       url(r'^api/donate/', DonateView.as_view()),
       url(r'^api/volunteer/', VolunteerAjax.as_view()),
       url(r'^api/contact/', ContactAjax.as_view()),
       url(r'^api/audio/', RecordAudioAjax.as_view()),
       url(r'^api/', include(router.urls)),
       url(r'^api-auth/', include('rest_framework.urls')),
       # Django admin and favicons
       url(r'^admin/', admin.site.urls),

       # Backend file management system
       url(r'^filer/', include('filer.urls')),
       # Link to outmedia and static root
       url(r'^media/(?P<path>.*)$', serve, {'document_root': settings.MEDIA_ROOT}),
       url(r'^static/(?P<path>.*)$', serve, {'document_root': settings.STATIC_ROOT}),
       url(r'^taggit_autosuggest/', include('taggit_autosuggest.urls')),

       # Under development
       url(r'^invoicing/', include('invoicing.urls', namespace='invoicing')),
       url(r'^tracker/', include('tracker.urls')),
       # and finally the cms manager
       url(r'^', include('favicon.urls')),
       re_path(r'^', include('cms.urls')),

    ] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

'''
This product is open source but time was taken to put it together.
'''
