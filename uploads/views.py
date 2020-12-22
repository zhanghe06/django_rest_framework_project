# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from datetime import datetime

from rest_framework import viewsets
from rest_framework.decorators import action
from rest_framework.response import Response

from commons.paginations import ApiPagination
from uploads.models import Avatar
from uploads.serializers import AvatarSerializer


class AvatarViewSet(viewsets.ModelViewSet):
    """头像视图"""
    queryset = Avatar.objects.all()
    serializer_class = AvatarSerializer
    pagination_class = ApiPagination
    permission_classes = []

    @action(methods=['GET'], detail=False)
    def get_list(self, request, *args, **kwargs):
        """
        http://0.0.0.0:8000/uploads/avatar/get_list/
        """
        queryset = Avatar.objects.all()
        page = self.paginate_queryset(queryset)
        serializer_context = {'request': request}
        serializer = self.serializer_class(
            page, context=serializer_context, many=True
        )
        return self.get_paginated_response(serializer.data)

    @action(methods=['GET'], detail=True)
    def get_info(self, request, pk, *args, **kwargs):
        """
        http://0.0.0.0:8000/uploads/avatar/e35cb8ef-d32d-467a-80ba-a302ced698f0/get_info/
        """
        instance = Avatar.objects.get(pk=pk)
        serializer = self.serializer_class(instance)
        return Response(serializer.data)

    @action(methods=['POST'], detail=False)
    def add_info(self, request, *args, **kwargs):
        """
        http://0.0.0.0:8000/uploads/avatar/add_info/
        """
        serializer = self.serializer_class(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data)

    @action(methods=['GET', 'POST'], detail=True)
    def del_info(self, request, pk, *args, **kwargs):
        """
        http://0.0.0.0:8000/uploads/avatar/e35cb8ef-d32d-467a-80ba-a302ced698f0/del_info/
        """
        instance = Avatar.objects.get(pk=pk)
        instance.time_delete = datetime.utcnow()
        instance.save()
        return Response({'result': True})
