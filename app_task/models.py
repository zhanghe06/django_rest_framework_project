# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from commons.models import BaseModel


class School(BaseModel):
    name = models.CharField(max_length=16)

    class Meta:
        db_table = 'school'

    def __str__(self):
        return self.name or str(self.pk)


class Tag(BaseModel):
    name = models.CharField(max_length=16)

    class Meta:
        db_table = 'tag'

    def __str__(self):
        return self.name or str(self.pk)


class Student(BaseModel):
    name = models.CharField(max_length=8)
    school = models.ForeignKey(to=School, blank=True, null=True)
    state = models.BooleanField(default=True)
    tag = models.ManyToManyField(to=Tag, blank=True)

    class Meta:
        db_table = 'student'

    def __str__(self):
        return self.name or str(self.pk)

# class Avatar(BaseModel):
#     user = models.ForeignKey(Student, verbose_name='用户')
#     url = models.ImageField(upload_to='avatar/%Y%m%d', null=False, blank=False, verbose_name='图片')
#
#     class Meta:
#         db_table = 'avatar'
#         verbose_name = '头像'
#
#     def __str__(self):
#         return str(self.pk)
#
#
# class Document(BaseModel):
#     user = models.ForeignKey(Student, related_name='user_document', verbose_name='用户')
#     url = models.FileField(upload_to='document/%Y%m%d', null=False, blank=False, verbose_name='文档')
#
#     class Meta:
#         db_table = 'document'
#         verbose_name = '文档'
#
#     def __str__(self):
#         return str(self.pk)
