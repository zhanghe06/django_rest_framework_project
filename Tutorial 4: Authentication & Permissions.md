## Authentication & Permissions

http://www.django-rest-framework.org/tutorial/4-authentication-and-permissions/

```
$ rm -f tmp.db db.sqlite3
$ rm -r snippets/migrations
$ python manage.py makemigrations snippets
$ python manage.py migrate
```

create a few different users, to use for testing the API
```
$ python manage.py createsuperuser
Username (leave blank to use 'zhanghe'): user_01
Email address: user_01@example.com
Password: password01
Password (again): password01
Superuser created successfully.
$ python manage.py createsuperuser
Username (leave blank to use 'zhanghe'): user_02
Email address: user_02@example.com
Password: password02
Password (again): password02
Superuser created successfully.
```
