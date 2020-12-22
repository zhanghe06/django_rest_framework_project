# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-20 06:22
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('orders', '0002_auto_20200814_0758'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='user',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AlterField(
            model_name='order',
            name='code',
            field=models.CharField(default='', max_length=16),
        ),
        migrations.AlterField(
            model_name='orderitem',
            name='order',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_items', to='orders.Order'),
        ),
    ]
