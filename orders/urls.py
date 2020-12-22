#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: urls.py
@time: 2020-08-14 14:11
"""

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from orders.views import OrderViewSet

router = DefaultRouter()

router.register(prefix=r'order', viewset=OrderViewSet, basename='order')

urlpatterns = [
    url(r'^orders/', include(router.urls)),
]
