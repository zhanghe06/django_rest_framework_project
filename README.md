## django-rest-framework

[![Build Status](https://travis-ci.org/zhanghe06/django_rest_framework_project.svg?branch=master)](https://travis-ci.org/zhanghe06/django_rest_framework_project)
[![Coverage Status](https://coveralls.io/repos/github/zhanghe06/django_rest_framework_project/badge.svg?branch=master)](https://coveralls.io/github/zhanghe06/django_rest_framework_project?branch=master)

[http://www.django-rest-framework.org](http://www.django-rest-framework.org)

[https://github.com/encode/django-rest-framework](https://github.com/encode/django-rest-framework)


```
pip install djangorestframework
pip install django-celery
pip install django-excel
pip install django-filter
pip install httpie
pip install pygments
```

注意过滤器：
python 2.7版本不支持2.0以上版本
`pip install "django-filter<2.0"`


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

### custom authentication

http://python.usyiyi.cn/translate/django_182/topics/auth/customizing.html


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
# print
from __future__ import print_function

# unicode
from __future__ import unicode_literals

# Note: py2, 'xxx' >> b'xxx'; u'xxx' >> 'xxx'(option);

# division /, //
from __future__ import division
```


### migrate

```
python manage.py migrate                # 初始化数据库（应用默认数据）
python manage.py makemigrations <appname>   # 生成变更方案（Model -> migrations）
python manage.py migrate <appname>          # 更新到数据库（migrations -> DB）
```


### celery的crontab表达式

```
# -*- coding: utf-8 -*-

from celery.schedules import crontab
from celery.task import periodic_task

@periodic_task(run_every=crontab())
def some_task():
    print('periodic task test!!!!!')
```

表示每分钟0秒时刻执行一次（后面不提这个0秒，大家都知道就行了，省点口水）。
其中，crontab()实例化的时候没设置任何参数，都是使用默认值。crontab一共有7个参数，常用有5个参数分别为：

参数 | 说明 | 取值
--- | --- | ---
minute | 分钟 | 范围0-59
hour | 小时 | 范围0-23
day_of_week | 星期几 | 范围0-6。以星期天为开始，即0为星期天。这个星期几还可以使用英文缩写表示，例如“sun”表示星期天
day_of_month | 每月第几号 | 范围1-31
month_of_year | 月份 | 范围1-12

例子
```
# 每天1点0分，执行1次
crontab(minute=0, hour=1)
# 每小时0分，执行1次
crontab(minute=0, hour='*/1')

# 每2个小时中每分钟执行1次任务
crontab(hour='*/2')

# 每3个小时的0分时刻执行1次任务
# 即[0,3,6,9,12,15,18,21]点0分
crontab(minute=0, hour='*/3')

# 每3个小时或8点到12点的0分时刻执行1次任务
# 即[0,3,6,9,12,15,18,21]+[8,9,10,11,12]点0分
crontab(minute=0, hour='*/3,8-12')

# 每个季度的第1个月中，每天每分钟执行1次任务
# 月份范围是1-12，每3个月为[1,4,7,10]
crontab(month_of_year='*/3')

# 每月偶数天数的0点0分时刻执行1次任务
crontab(minute=0, hour=0, day_of_month='2-31/2')

# 每年5月11号的0点0分时刻执行1次任务
crontab(0, 0, day_of_month='11', month_of_year='5')
```


### 任务系统，基于django-celery

[https://pypi.org/project/django-celery](https://pypi.org/project/django-celery)

[https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html](https://docs.celeryproject.org/en/latest/django/first-steps-with-django.html)

查看数据
```
➜  django_rest_framework_project git:(master) ✗ sqlite3
sqlite> .database
main: /Users/zhanghe/code/django_rest_framework_project/db.sqlite3
sqlite> .tables
auth_group                  django_admin_log
auth_group_permissions      django_content_type
auth_permission             django_migrations
auth_user                   django_session
auth_user_groups            snippets_snippet
auth_user_user_permissions
```

```
django-admin.py startproject example        # 创建项目
python manage.py startapp app_task          # 创建应用


pip install django-celery
```

settings.py 补充：
```
import djcelery
djcelery.setup_loader()

INSTALLED_APPS += ("djcelery", )


# redis
# BROKER_BACKEND = 'redis'
# BROKER_URL = 'redis://127.0.0.1:6379/0'

# 根据需要修改下面app模块及任务模块
CELERY_IMPORTS = ('snippets.tasks', )
CELERY_TIMEZONE = TIME_ZONE
CELERYBEAT_SCHEDULER = 'djcelery.schedulers.DatabaseScheduler'

CELERY_ENABLE_UTC = True
CELERYD_MAX_TASKS_PER_CHILD = 3 #  每个worker最多执行3个任务就会被销毁，可防止内存泄露，默认是100
```


```
python manage.py migrate djcelery
```

查看数据(已经更新)
```
sqlite> .tables
auth_group                  django_migrations
auth_group_permissions      django_session
auth_permission             djcelery_crontabschedule
auth_user                   djcelery_intervalschedule
auth_user_groups            djcelery_periodictask
auth_user_user_permissions  djcelery_periodictasks
celery_taskmeta             djcelery_taskstate
celery_tasksetmeta          djcelery_workerstate
django_admin_log            snippets_snippet
django_content_type
```

查看命令
```
python manage.py celery
```

```
python manage.py celery worker  # 开启工作进程
python manage.py celery beat    # 开启定时调度
```

定时任务

参考：[https://www.cnblogs.com/crb912/p/8976937.html](https://www.cnblogs.com/crb912/p/8976937.html)


### F()

F函数，直接对字段进行操作，无需提前读取到内存

```
obj = Order.objects.get(orderid='12')
obj.amount += 1
obj.order.save()
```
重构为以下形式
```
from django.db.models import F
from core.models import Order

obj = Order.objects.get(orderid='12')
obj.amount = F('amount') + 1
obj.save()
```

### Q()

Q函数，可以用来构建复杂的查询条件

```
from django.db.models import Q
from functools import reduce
from operator import or_

filter_args = []
filter_kwargs = {}
name_args = reduce(or_, (Q(name__icontains=name) for name in name_list))
filter_args.append(name_args)
code_args = reduce(or_, (Q(code__icontains=code) for code in code_list))
filter_args.append(code_args)
Companies.objects.filter(*filter_args, **filter_kwargs)
```

exclude 排除
~Q() 否定


### model

定义
```
# 字符串
null=False, blank=True, default=''
# 时间
# 整型
```

增删改查
```
models.App.objects.create(**data)                        # 增
models.App.objects.filter(id=1).delete()                 # 删
models.App.objects.filter(**condition).update(**data)    # 改
models.App.objects.all()                                 # 查 - 列表
models.App.objects.filter(**condition).first()           # 查 - 详情
models.App.objects.filter(**condition).count()           # 查 - 计数
```

筛选条件（filter）
```
id__gt              # 大于
id__lt              # 小于
id__in              # 列表范围
id__range           # 起止范围
name__contains      # 模糊匹配
name__icontains     # 模糊匹配 大小写不敏感
name__startswith    # 开始
name__istartswith   # 开始 大小写不敏感
name__endswith      # 结尾
name__iendswith     # 结尾 大小写不敏感
time__year
time__month
time__day
time__date
```

不等于
```
from django.db.models import Q
myapps = models.App.objects.filter(~Q(name=''))
```

分组（group by）
```
from django.db.models import Count, Min, Max, Sum
models.App.objects.filter(name=1).values('id').annotate(c=Count('num'))
# SELECT "app"."id", COUNT("app"."num") AS "c" FROM "app" WHERE "app"."name" = 1 GROUP BY "app"."id"
```

排序（order by）
```
models.App.objects.filter(**condition).order_by('id')    # asc
models.App.objects.filter(**condition).order_by('-id')   # desc
```

含有 choices 字段，使用`get_%s_display`可以显示值

serializer 中，可以使用：
```
tag_display = serializers.CharField(source='get_tag_display', read_only=True)
```

update_or_create
```
update_or_create(defaults=None, **kwargs)
kwargs是查询条件; defaults是更新内容
通过kwargs能查询到记录，则将defaults更新到记录，否则结合defaults创建新记录

例
Member.objects.update_or_create(defaults={'field1': 1,'field2': 2}, **{'user': 1})
当存在user=1时，则更新，不存在则创建
```

事务
```
from django.db import transaction
```

```
with transation.atomic:
    #do something and commit the transaction
    transaction.on_commit(lambda: some_celery_task.delay('arg1'))
```

### 联表查询（与SQLAlchemy不同，Django没有join方法）

`User`、`Role`

- 一对多 1:N
```
class User(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)
    role = models.ForeignKey('Role')

class Role(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)
```

正向查找
```
models.User.objects.filter(**condition).first().Role.name
```

反向查找

- 多对多 N:N
```
class Host(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=32)

class Group(models.Model):
    id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=16)

class HostToGroup(models.Model):
    id = models.AutoField(primary_key=True)
    host = models.ForeignKey(‘Host‘)
    group = models.ForeignKey(‘Group‘)
```

### select_related


### prefetch_related


### serializers

序列化器

作用: 序列化/反序列化

- 请求校验
- 响应格式

序列化和反序列化可以复用
增：效验请求数据 > 执行反序列化过程 > 保存数据库 > 将保存的对象序列化并返回
删：判断要删除的数据是否存在 > 执行数据库删除
改：判断要修改的数据是否存在 > 效验请求的参数 > 执行反序列化过程 > 保存数据库 > 将保存的对象序列化并返回
查：查询数据库 > 将数据序列化并返回


django rest framework serializer中获取request:

views.py
```
serializer = self.get_serializer(data=request.data, context={'request': request})
serializer.is_valid(raise_exception=True)
```

serializers.py
```
class TestSerializer(serializers.ModelSerializer):
    user_name = serializers.SerializerMethodField()  # 用户名称

    def get_user_name(self, obj):
        return self.context['request'].user.name

    class Meta:
        model = Test
        fields = (
            'id',
            'user_name',
        )
```

实例
```
serializer = TestSerializer(Test.objects.first())
serializer.data
```

集合
```
serializer = TestSerializer(Test.objects.all(), many=True)
serializer.data
```

### ViewSet 视图集

action

使用`rest_framework.decorators.action`装饰器，自定义的动作生成路由

以action装饰器装饰的方法名会作为action动作名，与list、retrieve等同。

action装饰器可以接收两个参数：
```
methods: 声明该action对应的请求方式，列表传递
detail: 声明该action的路径是否与单一资源对应，及是否是xxx/<pk>/action方法名/
    True 表示路径格式是xxx/<pk>/action方法名/
    False 表示路径格式是xxx/action方法名/
```

### signals 信号

Model signals


django.db.models.signals.pre_init | pre_init(sender, args, kwargs)
django.db.models.signals.post_init | post_init(sender, instance)
django.db.models.signals.pre_save | pre_save(sender, instance, raw, using, update_fields)
django.db.models.post_save | post_save(sender, instance, created, raw, using, update_fields)
django.db.models.signals.pre_delete | pre_delete(sender, instance, using)
django.db.models.signals.post_delete | post_delete(sender, instance, using)
django.db.models.signals.m2m_changed | -


Request/response signals

django.core.signals.request_started | request_started(sender, environ)
django.core.signals.request_finished | -
django.core.signals.got_request_exception | -


以main模块为例

`main/__init__.py`
```
default_app_config = 'main.apps.MainConfig'
```

`main/apps.py`
```
from django.apps import AppConfig


class MainConfig(AppConfig):
    name = 'main'

    def ready(self):
        print('我被执行了！')
```

`main/signals.py`
```
def callback_init(sender, **kwargs):
    pass
```


### 修改自定义用户类

一、创建自定义用户模型 users/models.py
```
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    username = models.CharField(max_length=20, null=False, blank=True, default='', verbose_name='姓名')
    email = models.CharField(max_length=64, null=False, blank=True, default='', verbose_name='邮箱')
    image = models.ImageField(max_length=100, upload_to='image/%Y/%m', null=False, blank=True, default='image?default.png', verbose_name='头像')

    class Meta:
    　　verbose_name = '用户信息'

　　def __str__(self):
    　　return self.username

```

二、指定自定义用户模型配置 settings.py
```
AUTH_USER_MODE = 'users.CustomUser'
```

三、修改认证系统用以支持自定义模型 users/backends.py
```
from django.contrib.auth.backends import ModelBackend

class CustomBackend(ModelBackend):
    def authenticate(self, username=None, password=None, **kwargs):
        try:
            user = UserProfile.objects.get(Q(username = username) | Q(email=username))
            if user.check_password(password):
                return user
        except Exception as e:
            return None
```

四、指定自定义用户认证配置 settings.py
```
AUTHENTICATION_BACKENDS = ('users.backends.CustomBackend',)
```


### Django Admin

配置
```
from django.contrib import admin

admin.site.site_header = '后台管理系统'   # 设置页面头部名称
admin.site.site_title = '后台管理系统'    # 设置浏览器的标题
```

注册新的模型
```
from api import models
admin.site.register(models.CourseCategory)
```

创建管理用户
```
python manage.py createsuperuser
```

### 静态资源

DEBUG为False时，'django.contrib.staticfiles'会关闭，即Django不会自动搜索静态文件

1. 页面排版不正常，即css文件不能正常加载；
2. 通过url不能访问静态文件，如图片等。

- 调试模式(DEBUG = True)

settings.py
```
# Static files
STATIC_URL = '/static/'
STATIC_ROOT = os.path.join(BASE_DIR, 'static')  # DEBUG = False (product model)

# Uploads files
MEDIA_URL = '/downloads/'
MEDIA_ROOT = os.path.join(BASE_DIR, 'downloads')
```

urls.py
```
from django.conf import settings
from django.conf.urls.static import static

# ^downloads\/(?P<path>.*)$
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ^static\/(?P<path>.*)$
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
```

- 生产模式(DEBUG = False)

除了以上配置，还需要搜集静态资源文件
```
python manage.py collectstatic
```
从STATICFILES_DIRS搜集，存到STATIC_ROOT

必须配置 Nginx 或 Apache
```
location /downloads/ {
    root /Users/zhanghe/code/django_rest_framework_project/downloads;
}
```

当DEBUG = False，需要本地调试时，可以使用以下方式，此时静态资源不走static目录
```bash
python manage.py runserver --insecure
```


### 调试

[http://127.0.0.1:8000/user/api](http://127.0.0.1:8000/user/api)


### 排错

Fixing UnicodeEncodeError for file uploads
```
export LANG='en_US.UTF-8'
export LC_ALL='en_US.UTF-8'
```
