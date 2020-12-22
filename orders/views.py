# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from orders.models import Order, OrderItem
from orders.serializers import OrderSerializer
from commons.paginations import ApiPagination
from orders.services import OrderServices


class OrderViewSet(viewsets.ModelViewSet):
    """订单视图"""
    queryset = Order.objects.filter()
    serializer_class = OrderSerializer
    pagination_class = ApiPagination
    permission_classes = []
    service_class = OrderServices

    @action(methods=['GET'], detail=False)
    def get_list(self, request, *args, **kwargs):
        """
        http://0.0.0.0:8000/orders/order/get_list/
        """
        page = self.paginate_queryset(self.get_queryset())
        serializer_context = {'request': request}
        serializer = self.serializer_class(
            page, context=serializer_context, many=True
        )
        return self.get_paginated_response(serializer.data)

    @action(methods=['GET'], detail=True)
    def get_info(self, request, pk, *args, **kwargs):
        """
        http://0.0.0.0:8000/orders/order/e35cb8ef-d32d-467a-80ba-a302ced698f0/get_info/
        """
        instance = Order.objects.get(pk=pk)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False)
    def add_info(self, request, *args, **kwargs):
        """
        http://0.0.0.0:8000/orders/order/add_info/
        {
            "code": "order_name_01",
            "order_items": [
                {
                    "name": "a",
                    "qty": 20,
                    "price": 100.00
                }
            ]
        }
        """
        serializer_context = {'request': request}
        serializer = self.serializer_class(data=request.data, context=serializer_context)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=['POST'], detail=True)
    def mod_info(self, request, pk, *args, **kwargs):
        """
        http://0.0.0.0:8000/orders/order/e35cb8ef-d32d-467a-80ba-a302ced698f0/mod_info/
        """
        instance = Order.objects.get(pk=pk)
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=['GET', 'POST'], detail=True)
    def del_info(self, request, pk, *args, **kwargs):
        """
        http://0.0.0.0:8000/orders/order/e35cb8ef-d32d-467a-80ba-a302ced698f0/del_info/
        """
        instance = Order.objects.get(pk=pk)
        instance.time_delete = datetime.utcnow()
        instance.save()
        return Response({'result': True})

    @action(methods=['POST'], detail=False)
    def add_info_service(self, request, *args, **kwargs):
        """
        http://0.0.0.0:8000/orders/order/add_info_service/
        {
            "code": "order_name_01",
            "order_items": [
                {
                    "name": "a",
                    "qty": 20,
                    "price": 100.00
                }
            ]
        }
        """
        service = self.service_class(request)
        data = service.create()
        return Response(data)
