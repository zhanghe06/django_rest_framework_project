# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-14 07:58
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='orderitem',
            name='qty',
            field=models.IntegerField(default=1),
        ),
    ]
