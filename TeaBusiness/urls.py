#!/usr/bin/env python
# -*- coding:utf-8 -*-
__author__ = 'yw'

from django.conf.urls import include, url
from django.contrib import admin
from .views import *

urlpatterns = [
    url(r'^$', index, name='index'),
    url(r'^list/$', product_list, name='product_list'),
    #url(r'^products/(?P<id>[^/]+)/edit', edit_product, name='edit_product'),
]