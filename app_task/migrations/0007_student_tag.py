# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-13 04:55
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ('app_task', '0006_auto_20200813_0252'),
    ]

    operations = [
        migrations.AddField(
            model_name='student',
            name='tag',
            field=models.ManyToManyField(to='app_task.Tag'),
        ),
    ]
