# coding=utf-8

from django.db import models
import django.utils.timezone as timezone
from django.core.urlresolvers import reverse

class BusinessList(models.Model):
    name = models.CharField('名称', max_length=50)
    title = models.CharField('标题', max_length=100)
    content = models.CharField('内容', max_length=1000)
    comments = models.CharField('评论', max_length=1000, null=True)
    plan_start_time = models.DateTimeField('计划开始时间', default=timezone.now)
    plan_end_time = models.DateTimeField('计划完成时间', null=True)
    plan_duration = models.DateTimeField('计划时长', null=True)
    create_time = models.DateTimeField('创建时间', auto_now=True)
    finish_time = models.DateTimeField('完成时间', null=True)
    latest_update_time = models.DateTimeField('状态更新时间', default=timezone.now)

    def __unicode__(self):
        return self.name + ":" + self.title

    def take_time(self):
        return self.finish_time - self.create_time if self.finish_time else None

    def finish_status(self):
        return 1 if self.finish_time else 0

class List(models.Model):
    def get_absolute_url(self):
        return reverse('view_list', args=[self.id])

class Item(models.Model):
    text = models.TextField(default='')
    list = models.ForeignKey(List, default=None)
