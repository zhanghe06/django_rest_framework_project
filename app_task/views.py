# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from django_filters.rest_framework import DjangoFilterBackend
from rest_framework import filters
from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from app_task.models import School, Tag, Student
from app_task.serializers import SchoolSerializer, TagSerializer, StudentSerializer
from commons.paginations import ApiPagination


class SchoolViewSet(viewsets.ModelViewSet):
    """学校视图"""
    queryset = School.objects.filter()
    # filter_backends =
    serializer_class = SchoolSerializer
    pagination_class = ApiPagination
    permission_classes = []

    @action(methods=['GET'], detail=False)
    def get_list(self, request, *args, **kwargs):
        """
        http://0.0.0.0:8000/app_task/school/get_list/
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
        http://0.0.0.0:8000/app_task/school/e35cb8ef-d32d-467a-80ba-a302ced698f0/get_info/
        """
        instance = School.objects.get(pk=pk)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False)
    def add_info(self, request, *args, **kwargs):
        """
        http://0.0.0.0:8000/app_task/school/add_info/
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=['POST'], detail=True)
    def mod_info(self, request, pk, *args, **kwargs):
        """
        http://0.0.0.0:8000/app_task/school/e35cb8ef-d32d-467a-80ba-a302ced698f0/mod_info/
        """
        instance = School.objects.get(pk=pk)
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=['GET', 'POST'], detail=True)
    def del_info(self, request, pk, *args, **kwargs):
        """
        http://0.0.0.0:8000/app_task/school/e35cb8ef-d32d-467a-80ba-a302ced698f0/del_info/
        """
        instance = School.objects.get(pk=pk)
        instance.time_delete = datetime.utcnow()
        instance.save()
        return Response({'result': True})


class TagViewSet(viewsets.ModelViewSet):
    """标签视图"""
    queryset = Tag.objects.filter()
    # filter_backends =
    serializer_class = TagSerializer
    pagination_class = ApiPagination
    permission_classes = []

    @action(methods=['GET'], detail=False)
    def get_list(self, request, *args, **kwargs):
        """
        http://0.0.0.0:8000/app_task/tag/get_list/
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
        http://0.0.0.0:8000/app_task/tag/e35cb8ef-d32d-467a-80ba-a302ced698f0/get_info/
        """
        instance = Tag.objects.get(pk=pk)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False)
    def add_info(self, request, *args, **kwargs):
        """
        http://0.0.0.0:8000/app_task/tag/add_info/
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=['POST'], detail=True)
    def mod_info(self, request, pk, *args, **kwargs):
        """
        http://0.0.0.0:8000/app_task/tag/e35cb8ef-d32d-467a-80ba-a302ced698f0/mod_info/
        """
        instance = Tag.objects.get(pk=pk)
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=['GET', 'POST'], detail=True)
    def del_info(self, request, pk, *args, **kwargs):
        """
        http://0.0.0.0:8000/app_task/tag/e35cb8ef-d32d-467a-80ba-a302ced698f0/del_info/
        """
        instance = Tag.objects.get(pk=pk)
        instance.time_delete = datetime.utcnow()
        instance.save()
        return Response({'result': True})


class StudentViewSet(viewsets.ModelViewSet):
    """学生视图"""
    queryset = Student.objects.all()
    serializer_class = StudentSerializer
    pagination_class = ApiPagination
    permission_classes = []
    # ordering = ('name',)

    @action(methods=['GET'], detail=False)
    def get_list(self, request, *args, **kwargs):
        """
        http://0.0.0.0:8000/app_task/student/get_list/
        """
        name = request.query_params.get('name')
        if name:
            self.queryset = Student.objects.filter(name=name)
        page = self.paginate_queryset(self.get_queryset())
        serializer_context = {'request': request}
        serializer = self.serializer_class(
            page, context=serializer_context, many=True
        )
        return self.get_paginated_response(serializer.data)

    @action(methods=['GET'], detail=True)
    def get_info(self, request, pk, *args, **kwargs):
        """
        http://0.0.0.0:8000/app_task/student/e35cb8ef-d32d-467a-80ba-a302ced698f0/get_info/
        """
        instance = Student.objects.get(pk=pk)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False)
    def add_info(self, request, *args, **kwargs):
        """
        http://0.0.0.0:8000/app_task/student/add_info/
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=['POST'], detail=True)
    def mod_info(self, request, pk, *args, **kwargs):
        """
        http://0.0.0.0:8000/app_task/student/e35cb8ef-d32d-467a-80ba-a302ced698f0/mod_info/
        """
        instance = Student.objects.get(pk=pk)
        serializer = self.serializer_class(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=['GET', 'POST'], detail=True)
    def del_info(self, request, pk, *args, **kwargs):
        """
        http://0.0.0.0:8000/app_task/student/e35cb8ef-d32d-467a-80ba-a302ced698f0/del_info/
        """
        instance = Student.objects.get(pk=pk)
        instance.time_delete = datetime.utcnow()
        instance.save()
        return Response({'result': True})
