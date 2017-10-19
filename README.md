## django-rest-framework

http://www.django-rest-framework.org/

https://github.com/encode/django-rest-framework

```
$ virtualenv django_rest.env
$ source django_rest.env/bin/activate
$ pip install django
$ pip install djangorestframework
$ pip install markdown
$ pip install django-filter
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
