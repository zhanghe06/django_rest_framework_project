## django-rest-framework

[![Build Status](https://travis-ci.org/zhanghe06/django_rest_framework_project.svg?branch=master)](https://travis-ci.org/zhanghe06/django_rest_framework_project)
[![Coverage Status](https://coveralls.io/repos/github/zhanghe06/django_rest_framework_project/badge.svg?branch=master)](https://coveralls.io/github/zhanghe06/django_rest_framework_project?branch=master)

http://www.django-rest-framework.org/

https://github.com/encode/django-rest-framework

```
$ virtualenv django_rest.env
$ source django_rest.env/bin/activate
$ pip install django
$ pip install djangorestframework
$ pip install markdown
$ pip install django-filter
$ pip install coverage                      # OPTION (UnitTest Coverage)
$ django-admin.py startproject example .
$ ./manage.py migrate
$ ./manage.py createsuperuser
Username (leave blank to use 'zhanghe'): admin
Email address: admin@example.com
Password: 1234!@#$
Password (again): 1234!@#$
```

example/settings.py
example/urls.py

```
$ ./manage.py runserver
```

http://0.0.0.0:8000/admin
http://0.0.0.0:8000

list the users endpoint:
```
$ curl -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/users/
[
    {
        "url": "http://127.0.0.1:8000/users/1/",
        "username": "admin",
        "email": "admin@example.com",
        "is_staff": true
    }
]

$ curl -H 'Accept: application/json; indent=4' -u 'admin:1234!@#$' http://127.0.0.1:8000/users/
[
    {
        "url": "http://127.0.0.1:8000/users/1/",
        "username": "admin",
        "email": "admin@example.com",
        "is_staff": true
    }
]
```

create a new user
```
$ curl -X POST -d username=new -d email=new@example.com -d is_staff=false -H 'Accept: application/json; indent=4' http://127.0.0.1:8000/users/
{
    "detail": "Authentication credentials were not provided."
}

$ curl -X POST -d username=new -d email=new@example.com -d is_staff=false -H 'Accept: application/json; indent=4' -u 'admin:1234!@#$' http://127.0.0.1:8000/users/
{
    "url": "http://127.0.0.1:8000/users/2/",
    "username": "new",
    "email": "new@example.com",
    "is_staff": false,
}
```

### DjangoFilterBackend

install `django-filter`
```
$ pip install django-filter
```

Then add `django_filters` to Django's `INSTALLED_APPS`
```
INSTALLED_APPS = [
    ...
    'django_filters'
]
```

add the filter backend to project's settings
```
REST_FRAMEWORK = {
    'DEFAULT_FILTER_BACKENDS': ('django_filters.rest_framework.DjangoFilterBackend',)
}
```

### UnitTest and Coverage

```
$ python manage.py test snippets
```

```
$ coverage run --source='.' manage.py test
$ coverage report
Name                                  Stmts   Miss  Cover
---------------------------------------------------------
example/__init__.py                       0      0   100%
example/settings.py                      19      0   100%
example/urls.py                           9      0   100%
manage.py                                 2      0   100%
snippets/__init__.py                      0      0   100%
snippets/admin.py                         2      0   100%
snippets/apps.py                          4      0   100%
snippets/migrations/0001_initial.py       8      0   100%
snippets/migrations/__init__.py           0      0   100%
snippets/models.py                       28      6    79%
snippets/permissions.py                   7      3    57%
snippets/serializers.py                  15      0   100%
snippets/tests.py                         8      0   100%
snippets/urls.py                         18     18     0%
snippets/views.py                        34      4    88%
---------------------------------------------------------
TOTAL                                   154     31    80%
```


### PY2 & PY3

Py3's code still running on Python 2.7

```python
# unicode
from __future__ import unicode_literals

# division /, //
from __future__ import division
```
