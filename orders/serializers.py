#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: serializers.py
@time: 2020-08-14 13:09
"""

from rest_framework import serializers

from orders.models import Order, OrderItem


class OrderItemSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        print(validated_data)
        return OrderItem.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    class Meta:
        model = OrderItem
        fields = ('id', 'name', 'qty', 'price')
        extra_kwargs = {'id': {'read_only': True}}


class OrderSerializer(serializers.ModelSerializer):
    order_items = OrderItemSerializer(many=True)

    def create(self, validated_data):
        print(validated_data)
        request = self.context.get('request')
        validated_data['user'] = request.user.username if request else ''

        # ManyToOne 关系处理
        order_items = []
        if 'order_items' in validated_data:
            order_items = validated_data.pop('order_items')

        instance = Order.objects.create(**validated_data)

        for order_item in order_items:
            order_item['order_id'] = instance.pk
            OrderItem.objects.create(**order_item)

        instance.save()
        return instance

    def update(self, instance, validated_data):
        # ManyToOne 关系处理
        order_items = []
        mod_items = False  # 修改明细标识
        if 'order_items' in validated_data:
            mod_items = True
            order_items = validated_data.pop('order_items')
            # 清空历史
            OrderItem.objects.filter(order_id=instance.pk).delete()

        instance.code = validated_data.get('code', instance.code)
        instance.save()

        # 重建明细
        if mod_items:
            for order_item in order_items:
                order_item['order_id'] = instance.pk
                OrderItem.objects.create(**order_item)

        return instance

    class Meta:
        model = Order
        fields = ('id', 'code', 'user', 'order_items', 'time_create', 'time_update')
        extra_kwargs = {'id': {'read_only': True}}
