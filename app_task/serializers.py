#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: serializers.py
@time: 2020-08-11 20:09
"""

from rest_framework import serializers

from app_task.models import School, Tag, Student


class SchoolSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        # 测试
        # return School(**validated_data)
        # 写库
        return School.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        # 测试
        # return instance
        # 写库
        instance.save()
        return instance

    class Meta:
        model = School
        fields = ('id', 'name', 'time_create', 'time_update')
        extra_kwargs = {'id': {'read_only': True}}


class TagSerializer(serializers.ModelSerializer):

    def create(self, validated_data):
        print(validated_data)
        return Tag.objects.create(**validated_data)

    def update(self, instance, validated_data):
        instance.name = validated_data.get('name', instance.name)
        instance.save()
        return instance

    class Meta:
        model = Tag
        fields = ('id', 'name')
        extra_kwargs = {'id': {'read_only': True}}


class StudentSerializer(serializers.ModelSerializer):
    school_name = serializers.ReadOnlyField(source='school.name', default='')
    time_create = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    time_update = serializers.DateTimeField(format="%Y-%m-%d %H:%M:%S", read_only=True)
    # 只读显示主键
    # tags = serializers.PrimaryKeyRelatedField(source='tag', many=True, read_only=True)
    # 只读显示名称
    tags = serializers.SlugRelatedField(source='tag', many=True, read_only=True, slug_field='name')

    # 显示整体结构
    # tags = TagSerializer(source='tag', many=True, required=False)

    def create(self, validated_data):
        print(validated_data)
        # ManyToManyField 关系处理
        tag = []
        if 'tag' in validated_data:
            tag = validated_data.pop('tag')

        instance = Student.objects.create(**validated_data)

        instance.tag = tag
        instance.save()
        return instance

    def update(self, instance, validated_data):
        # if 'name' in validated_data:
        #     instance.name = validated_data.get('name')
        # if 'school' in validated_data:
        #     instance.school = validated_data.get('school')
        # if 'tag' in validated_data:
        #     instance.tag = validated_data.get('tag')
        for attr, value in validated_data.items():
            setattr(instance, attr, value)
        instance.save()
        return instance

    class Meta:
        model = Student
        fields = ('id', 'name', 'school', 'school_name', 'tag', 'tags', 'time_create', 'time_update')
        extra_kwargs = {
            'id': {'read_only': True},
            'school': {'write_only': True},
            'tag': {'write_only': True},
            'time_create': {'read_only': True},
            'time_update': {'read_only': True},
        }

# class AvatarListSerializer(serializers.Serializer):
#     imgs = serializers.ListField(
#         child=serializers.FileField(max_length=100000,
#                                     allow_empty_file=False,
#                                     use_url=True), write_only=True
#     )
#     blog_imgs = serializers.ListField(
#         child=serializers.CharField(max_length=1000,),read_only=True
#     )
#
#     def create(self, validated_data):
#         files = validated_data.get('files')
#         images = []
#         for index, url in enumerate(files):
#             image = Avatar.objects.create(url=url, user=Student.objects.get(id=self.context['request'].user.id))
#             instance = AvatarSerializer(image, context=self.context)
#             images.append(instance.data['url'])
#         return {'blog_imgs': images}
#
#     def update(self, instance, validated_data):
#         pass
