# -*- coding: utf-8 -*-
from __future__ import absolute_import, print_function, unicode_literals

from django.contrib import admin
from rest_framework import routers

from .views import UserViewSet, PageViewSet, PostViewSet

# Routers provide an easy way of automatically determining the URL conf.


router = routers.DefaultRouter()

router.register(r'users', UserViewSet)
router.register(r'pages', PageViewSet)
router.register(r'post', PostViewSet)

admin.autodiscover()
