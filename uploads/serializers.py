#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: serializers.py
@time: 2020-08-14 00:33
"""

from rest_framework import serializers
from uploads.models import Avatar


class AvatarSerializer(serializers.ModelSerializer):
    # user = serializers.HiddenField(default=serializers.CurrentUserDefault())
    # user_name = serializers.ReadOnlyField(source='user.name', default='')

    def __str__(self):
        return str(self.pk)

    def create(self, validated_data):
        print(validated_data)
        file_instance = validated_data.get('file')
        data_extension = {
            'name': file_instance.name,
            'size': file_instance.size,
            'content_type': file_instance.content_type,
        }
        validated_data.update(**data_extension)
        return Avatar.objects.create(**validated_data)

    class Meta:
        model = Avatar
        fields = ('id', 'name', 'size', 'content_type', 'file')
        extra_kwargs = {
            'id': {'read_only': True},
            'name': {'read_only': True},
            'size': {'read_only': True},
            'content_type': {'read_only': True},
        }
