# -*- coding:utf-8 -*-
from django.db import models
import datetime

# Create your models here.
class Products(models.Model):
    name = models.CharField(u'商品名称',max_length=50)
    description = models.CharField(u'商品描述',max_length=200)
    image_url = models.CharField(u'商品图片',max_length=200)
    created = models.DateTimeField(u'上架时间',auto_now_add=True)
    price = models.DecimalField(u'价格',max_digits=8, decimal_places=2)
    price_market = models.DecimalField(u'市场价',max_digits=8, decimal_places=2)
    weight = models.CharField(u'重量',max_length=5)
    feature = models.CharField(u'特征',max_length=30)