"""example URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf import settings
from django.conf.urls.static import static
from django.contrib import admin

from django.conf.urls import url, include
# from django.contrib.auth.models import User
# from rest_framework import serializers, viewsets, routers


# # Serializers define the API representation.
# class UserSerializer(serializers.HyperlinkedModelSerializer):
#     class Meta:
#         model = User
#         fields = ('url', 'username', 'email', 'is_staff')
#
#
# # ViewSets define the view behavior.
# class UserViewSet(viewsets.ModelViewSet):
#     queryset = User.objects.all()
#     serializer_class = UserSerializer
#
#
# # Routers provide a way of automatically determining the URL conf.
# router = routers.DefaultRouter()
# router.register(r'users', UserViewSet)


# Tutorial 6: ViewSets & Routers
# --------------------
from snippets import views
from rest_framework.routers import DefaultRouter
from app_task.urls import urlpatterns as app_task_urlpatterns
from uploads.urls import urlpatterns as uploads_urlpatterns
from orders.urls import urlpatterns as orders_urlpatterns

# Create a router and register our viewsets with it.
router = DefaultRouter()
router.register(r'snippets', views.SnippetViewSet)
router.register(r'users', views.UserViewSet)

# Wire up our API using automatic URL routing.
# Additionally, we include login URLs for the browsable API.
urlpatterns = [
    url(r'^', include(router.urls)),
    # url(r'^', include('snippets.urls')),
    url(r'^admin/', admin.site.urls),
]

urlpatterns += [
    url(r'^api-auth/', include('rest_framework.urls', namespace='rest_framework')),
]

urlpatterns += app_task_urlpatterns
urlpatterns += uploads_urlpatterns
urlpatterns += orders_urlpatterns

# ^downloads\/(?P<path>.*)$
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
# ^static\/(?P<path>.*)$
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
