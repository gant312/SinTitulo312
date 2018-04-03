# -*- encoding:utf-8 -*-

from django.conf.urls import url, include
from django.contrib import admin
from Usuarios import urls
import Usuarios

urlpatterns = [
    url(r'^home/$',include(Usuarios.urls), name='home')

]