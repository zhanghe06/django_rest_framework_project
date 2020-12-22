# -*- coding: utf-8 -*-

from __future__ import absolute_import

from celery import shared_task
from celery.schedules import crontab
from celery.task import periodic_task


@shared_task
def add(x, y):
    return x + y


@shared_task
def mul(x, y):
    return x * y


@shared_task
def xsum(numbers):
    return sum(numbers)


@periodic_task(run_every=crontab(minute='*/1'))
def some_task():
    print('periodic task test!')
