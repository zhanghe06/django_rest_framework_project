# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-13 08:46
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app_task', '0016_auto_20200813_0624'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='avatar',
            field=models.CharField(blank=True, max_length=128),
        ),
    ]
