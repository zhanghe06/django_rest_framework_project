# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib.auth.models import AnonymousUser, User
from django.test import TestCase
from rest_framework import status


# Create your tests here.

from .models import Snippet
from django.urls import reverse

test_user_data = [
    {
        'username': 'user_01',
        'email': 'user_01@example.com',
        'password': 'password01'
    },
    {
        'username': 'user_02',
        'email': 'user_02@example.com',
        'password': 'password02'
    },
]

test_snippet_data = [
    {
        'id': 1,
        'code': 'print 123'
    },
    {
        'id': 2,
        'code': 'print 456'
    },
]


class SnippetListViewTests(TestCase):

    def setUp(self):
        super(SnippetListViewTests, self).setUp()

        # create test user
        for index, user_item in enumerate(test_user_data):
            user_obj = 'user_%2d' % (index + 1)
            setattr(self, user_obj, User.objects.create_user(**user_item))
            # print('new user id: %s' % getattr(self, user_obj).id)

        # create test data
        for index, snippet_item in enumerate(test_snippet_data):
            user_obj = 'user_%2d' % (index + 1)
            owner_data = {'owner': getattr(self, user_obj)}
            snippet_item.update(owner_data)
            snippet = Snippet(**snippet_item)
            snippet.save()
            self.assertEqual(getattr(snippet, 'id'), index + 1)

    def test_snippet_list(self):
        """
        test snippet list
        """
        test_url = reverse('snippet-list')

        response = self.client.get(test_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response._headers.get('content-type'), ('Content-Type', 'application/json'))
        self.assertEqual(len(response.json().get('results', [])), len(test_snippet_data))


class SnippetDetailViewTests(TestCase):

    def setUp(self):
        super(SnippetDetailViewTests, self).setUp()

        # create test user
        for index, user_item in enumerate(test_user_data):
            user_obj = 'user_%2d' % (index + 1)
            setattr(self, user_obj, User.objects.create_user(**user_item))
            # print('new user id: %s' % getattr(self, user_obj).id)

        # create test data
        for index, snippet_item in enumerate(test_snippet_data):
            user_obj = 'user_%2d' % (index + 1)
            owner_data = {'owner': getattr(self, user_obj)}
            snippet_item.update(owner_data)
            snippet = Snippet(**snippet_item)
            snippet.save()
            self.assertEqual(getattr(snippet, 'id'), index + 1)

    def test_snippet_detail_failure(self):
        """
        test snippet detail
        """
        test_url = reverse('snippet-detail', kwargs={'pk': 100})

        response = self.client.get(test_url)
        self.assertEqual(response.status_code, status.HTTP_404_NOT_FOUND)
        self.assertEqual(response._headers.get('content-type'), ('Content-Type', 'application/json'))

    def test_snippet_detail_success(self):
        """
        test snippet detail
        """
        test_url = reverse('snippet-detail', kwargs={'pk': 1})

        response = self.client.get(test_url)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertEqual(response._headers.get('content-type'), ('Content-Type', 'application/json'))
