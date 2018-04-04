# -*- encoding:utf-8 -*-
from django.conf.urls import url
from .views import nose
urlpatterns = [
   url(r'^registro/$', nose.as_view(), name='registro')
]