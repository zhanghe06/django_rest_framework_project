# -*- coding: utf-8 -*-
# Generated by Django 1.11.29 on 2020-08-11 16:26
from __future__ import unicode_literals

import uuid

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='School',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('time_delete', models.DateTimeField(blank=True, null=True)),
                ('time_create', models.DateTimeField()),
                ('time_update', models.DateTimeField()),
                ('name', models.CharField(max_length=16)),
            ],
            options={
                'db_table': 'school',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, primary_key=True, serialize=False)),
                ('time_delete', models.DateTimeField(blank=True, null=True)),
                ('time_create', models.DateTimeField()),
                ('time_update', models.DateTimeField()),
                ('name', models.CharField(max_length=8)),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app_task.School')),
            ],
            options={
                'db_table': 'student',
            },
        ),
    ]
