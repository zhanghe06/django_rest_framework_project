#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: models.py
@time: 2020-08-14 00:19
"""


import uuid

from django.db import models


class BaseModel(models.Model):
    # https://www.django-rest-framework.org/api-guide/fields/#uuidfield
    id = models.UUIDField(max_length=36, primary_key=True, default=uuid.uuid4)
    time_delete = models.DateTimeField(blank=True, null=True)
    time_create = models.DateTimeField(auto_now_add=True)
    time_update = models.DateTimeField(auto_now=True)
    objects = models.Manager()

    class Meta:
        """抽象类, 公共模型必加"""
        abstract = True
