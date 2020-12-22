#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: urls.py
@time: 2020-08-14 00:29
"""


from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from uploads.views import AvatarViewSet

router = DefaultRouter()
router.register(prefix=r'avatar', viewset=AvatarViewSet, basename='avatar')

urlpatterns = [
    url(r'^uploads/', include(router.urls)),
]
