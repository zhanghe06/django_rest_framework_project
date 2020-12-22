# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

from commons.models import BaseModel


class Category(models.Model):
    """
    产品分类
    """
    CATEGORY_LEVEL = (
        (1, '一级类目'),
        (2, '二级类目'),
        (3, '三级类目'),
    )

    name = models.CharField(verbose_name='分类名称', default='', max_length=16)
    code = models.CharField(verbose_name='分类编码', default='', max_length=16)
    desc = models.TextField(verbose_name='类别描述', default='', help_text='类别描述')
    category_level = models.IntegerField('分类级别', choices=CATEGORY_LEVEL, help_text='分类级别')
    # 设置models有一个指向自己的外键
    parent_category = models.ForeignKey(to='self', on_delete=models.CASCADE, null=True, blank=True, verbose_name='父级分类',
                                        related_name='sub_cat')
    is_tab = models.BooleanField(verbose_name='是否导航', default=False, help_text='是否导航')

    class Meta:
        verbose_name = '产品分类'

    def __str__(self):
        return self.name


class Order(BaseModel):
    code = models.CharField(max_length=16, default='')
    user = models.CharField(max_length=16, default='')

    class Meta:
        db_table = 'order'

    def __str__(self):
        return self.code or str(self.pk)


class OrderItem(BaseModel):
    order = models.ForeignKey(to=Order, null=False, related_name='order_items')
    name = models.CharField(max_length=8)
    qty = models.IntegerField(default=1)
    price = models.DecimalField(max_digits=10, decimal_places=2, default=0)
    state = models.BooleanField(default=True)

    class Meta:
        db_table = 'order_item'

    def __str__(self):
        return self.name or str(self.pk)
