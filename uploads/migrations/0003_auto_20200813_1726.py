# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-13 17:26
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('uploads', '0002_auto_20200813_1639'),
    ]

    operations = [
        migrations.AddField(
            model_name='avatar',
            name='content_type',
            field=models.CharField(default='', max_length=32, verbose_name='\u6587\u4ef6\u7c7b\u578b'),
        ),
        migrations.AddField(
            model_name='avatar',
            name='size',
            field=models.PositiveIntegerField(default=0, verbose_name='\u6587\u4ef6\u5927\u5c0f'),
        ),
        migrations.AlterField(
            model_name='avatar',
            name='name',
            field=models.CharField(default='', max_length=64, verbose_name='\u6587\u4ef6\u540d\u79f0'),
        ),
    ]
