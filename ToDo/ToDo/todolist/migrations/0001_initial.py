# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BusinessList',
            fields=[
                ('id', models.AutoField(verbose_name='ID', serialize=False, auto_created=True, primary_key=True)),
                ('name', models.CharField(max_length=50, verbose_name=b'\xe5\x90\x8d\xe7\xa7\xb0')),
                ('title', models.CharField(max_length=100, verbose_name=b'\xe6\xa0\x87\xe9\xa2\x98')),
                ('content', models.CharField(max_length=1000, verbose_name=b'\xe5\x86\x85\xe5\xae\xb9')),
                ('comments', models.CharField(max_length=1000, null=True, verbose_name=b'\xe8\xaf\x84\xe8\xae\xba')),
                ('plan_start_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe8\xae\xa1\xe5\x88\x92\xe5\xbc\x80\xe5\xa7\x8b\xe6\x97\xb6\xe9\x97\xb4')),
                ('plan_end_time', models.DateTimeField(null=True, verbose_name=b'\xe8\xae\xa1\xe5\x88\x92\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xb6\xe9\x97\xb4')),
                ('plan_duration', models.DateTimeField(null=True, verbose_name=b'\xe8\xae\xa1\xe5\x88\x92\xe6\x97\xb6\xe9\x95\xbf')),
                ('create_time', models.DateTimeField(auto_now=True, verbose_name=b'\xe5\x88\x9b\xe5\xbb\xba\xe6\x97\xb6\xe9\x97\xb4')),
                ('finish_time', models.DateTimeField(null=True, verbose_name=b'\xe5\xae\x8c\xe6\x88\x90\xe6\x97\xb6\xe9\x97\xb4')),
                ('latest_update_time', models.DateTimeField(default=django.utils.timezone.now, verbose_name=b'\xe7\x8a\xb6\xe6\x80\x81\xe6\x9b\xb4\xe6\x96\xb0\xe6\x97\xb6\xe9\x97\xb4')),
            ],
        ),
    ]
