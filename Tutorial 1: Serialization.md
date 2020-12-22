## Serialization

[http://www.django-rest-framework.org/tutorial/1-serialization](http://www.django-rest-framework.org/tutorial/1-serialization)

```
$ pip install pygments
$ python manage.py startapp snippets
```

snippets/models.py

```
$ python manage.py makemigrations snippets
$ python manage.py migrate
$ python manage.py shell
```

```
$ pip install httpie
$ http http://127.0.0.1:8000/snippets/
HTTP/1.0 200 OK
Content-Length: 222
Content-Type: application/json
Date: Wed, 18 Oct 2017 11:27:50 GMT
Server: WSGIServer/0.1 Python/2.7.12
X-Frame-Options: SAMEORIGIN

[
    {
        "code": "foo = \"bar\"\n",
        "id": 1,
        "language": "python",
        "linenos": false,
        "style": "friendly",
        "title": ""
    },
    {
        "code": "foo = \"bar\"",
        "id": 2,
        "language": "python",
        "linenos": false,
        "style": "friendly",
        "title": ""
    }
]

$ http http://127.0.0.1:8000/snippets/2/
HTTP/1.0 200 OK
Content-Length: 108
Content-Type: application/json
Date: Wed, 18 Oct 2017 11:28:34 GMT
Server: WSGIServer/0.1 Python/2.7.12
X-Frame-Options: SAMEORIGIN

{
    "code": "foo = \"bar\"",
    "id": 2,
    "language": "python",
    "linenos": false,
    "style": "friendly",
    "title": ""
}
```


### 

正向：

反向：[https://www.django-rest-framework.org/api-guide/relations](https://www.django-rest-framework.org/api-guide/relations)
