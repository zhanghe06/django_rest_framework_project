# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from commons.models import BaseModel


class Avatar(BaseModel):
    name = models.CharField(max_length=64, verbose_name='文件名称', default='')
    size = models.PositiveIntegerField(verbose_name='文件大小', default=0)
    content_type = models.CharField(max_length=32, verbose_name='文件类型', default='')
    file = models.ImageField(upload_to='avatar/%Y%m%d', null=False, blank=False, verbose_name='文件地址')

    class Meta:
        db_table = 'avatar'
        verbose_name = '头像'

    def __str__(self):
        return str(self.pk)
