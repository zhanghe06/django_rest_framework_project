#!/usr/bin/env python
# encoding: utf-8

"""
@author: zhanghe
@software: PyCharm
@file: request_log.py
@time: 2020-02-20 19:35
"""
import json
import logging

from django.utils.deprecation import MiddlewareMixin


class RequestLogMiddleware(MiddlewareMixin):
    apiLogger = logging.getLogger('api')

    # def process_request(self, request):
    #     return None

    def process_response(self, request, response):
        try:
            body = json.loads(request.body)
        except Exception:
            body = dict()
        body.update(dict(request.POST))

        response = self.get_response(request)
        # if request.method != 'GET':
        self.apiLogger.info("{} {} {} {} {} {}".format(
            request.user, request.method, request.path, body,
            response.status_code, response.reason_phrase))
        return response
