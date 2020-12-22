#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: services.py
@time: 2020-08-20 14:18
"""

from orders.models import Order, OrderItem
from orders.serializers import OrderSerializer
from commons.paginations import ApiPagination


class OrderServices(object):
    def __init__(self, request=None):
        self.request = request
        self.serializer_context = {'request': request}
        pass

    def list(self):
        pass

    def create(self):
        serializer = OrderSerializer(data=self.request.data, context=self.serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return serializer.data


if __name__ == '__main__':
    pass
