#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: request_id.py
@time: 2020-02-18 03:40
"""

from uuid import uuid4
from django.utils.deprecation import MiddlewareMixin


class RequestIdMiddleware(MiddlewareMixin):
    request_id = ''

    def process_request(self, request):
        self.request_id = request.META.get('X-Request-Id', str(uuid4()))
        return None

    def process_response(self, request, response):
        response = self.get_response(request)
        response['X-Request-Id'] = self.request_id
        return response


if __name__ == '__main__':
    pass
