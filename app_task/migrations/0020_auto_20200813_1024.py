# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-13 10:24
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):
    dependencies = [
        ('app_task', '0019_auto_20200813_1020'),
    ]

    operations = [
        migrations.RenameField(
            model_name='avatar',
            old_name='user',
            new_name='student',
        ),
        migrations.RenameField(
            model_name='document',
            old_name='user',
            new_name='student',
        ),
    ]