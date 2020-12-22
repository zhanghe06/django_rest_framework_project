#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: request_id.py
@time: 2020-02-18 03:40
"""
from django.http import JsonResponse
from django.utils.deprecation import MiddlewareMixin
from rest_framework.response import Response
from rest_framework import status
from rest_framework.views import exception_handler


# 定义中间件类，处理全局异常
class ExceptionMiddleware(MiddlewareMixin):
    def process_exception(self, request, exception):
        response = JsonResponse({'message': '服务器内部错误'}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)
        return response

    def process_response(self, request, response):
        if response.status_code == 500:
            # response = self.get_response(request)
            return JsonResponse({"err": "500"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)

    def process_template_response(self, request, response):
        if response.status_code == 500:
            # response = self.get_response(request)
            return JsonResponse({"err": "500"}, status_code=status.HTTP_500_INTERNAL_SERVER_ERROR)


def custom_exception_handler(exc, context):
    """
    自定义异常处理
    :param exc: 别的地方抛的异常就会传给exc
    :param context: 字典形式。抛出异常的上下文(即抛出异常的出处;即抛出异常的视图)
    :return: Response响应对象
    """
    # 调用drf框架原生的异常处理方法,把异常和异常出处交给他处理,如果是序列化器异常就直接处理,处理之后就直接返回
    response = exception_handler(exc, context)
    # 如果响应为空表示不是序列化器异常,补充数据库异常
    if response is None:
        # view = context['view']
        # if isinstance(exc, DatabaseError) or isinstance(exc, RedisError):
        if isinstance(exc, Exception):
            # 数据库异常
            # logger.error('[%s] %s' % (view, exc))
            response = Response({'message': '服务器内部错误'}, status=status.HTTP_500_INTERNAL_SERVER_ERROR)
    return response
