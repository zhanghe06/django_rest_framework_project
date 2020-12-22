#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: urls.py
@time: 2020-08-11 23:11
"""

from django.conf.urls import url, include
from rest_framework.routers import DefaultRouter

from app_task.views import SchoolViewSet, TagViewSet, StudentViewSet

router = DefaultRouter()

router.register(prefix=r'school', viewset=SchoolViewSet, basename='school')
router.register(prefix=r'tag', viewset=TagViewSet, basename='tag')
router.register(prefix=r'student', viewset=StudentViewSet, basename='student')

urlpatterns = [
    url(r'^app_task/', include(router.urls)),
]
