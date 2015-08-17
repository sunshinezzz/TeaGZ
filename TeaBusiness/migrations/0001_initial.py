# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models, migrations


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Products',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name='\u5546\u54c1\u540d\u79f0')),
                ('description', models.CharField(max_length=200, verbose_name='\u5546\u54c1\u63cf\u8ff0')),
                ('image_url', models.CharField(max_length=200, verbose_name='\u5546\u54c1\u56fe\u7247')),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='\u4e0a\u67b6\u65f6\u95f4')),
                ('price', models.DecimalField(verbose_name='\u4ef7\u683c', max_digits=8, decimal_places=2)),
                ('price_market', models.DecimalField(verbose_name='\u5e02\u573a\u4ef7', max_digits=8, decimal_places=2)),
                ('weight', models.CharField(max_length=5, verbose_name='\u91cd\u91cf')),
                ('feature', models.CharField(max_length=30, verbose_name='\u7279\u5f81')),
            ],
        ),
    ]
