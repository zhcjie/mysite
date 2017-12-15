# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User
# Create your models here.

#栏目模型。
class ArticleColumn(models.Model):
    user = models.ForeignKey(User,related_name="article_column")# foreignkey：一对多
    column = models.CharField(max_length=200)
    created = models.DateField(auto_now_add=True)

    def __str__(self):
        return self.column

import os,django
from django.utils import timezone  # 与settings中时区设置有关
from django.core.urlresolvers import reverse
from slugify import slugify

#文章发布，创建数据模型类

class ArticlePost(models.Model):
    author = models.ForeignKey(User,related_name='article')
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=500)
    column = models.ForeignKey(ArticleColumn,related_name='article_column')
    body = models.TextField()
    created = models.DateTimeField(default=timezone.now) #得到文章发布的日期和时间。
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        # ordering = ('title',)
        ordering = ('-updated',)
        index_together = (('id','slug'),) #p127对数据库中这两个字段建立索引。提高读取对象打速度。

    def __str__(self):
        return self.title

    def save(self, *args, **kargs): #对原本save方法重写，为了实现下一句。
        self.slug = slugify(self.title) #1.
        super(ArticlePost,self).save(*args,**kargs)

    def get_absolute_url(self):#为了获取某篇文章对象打url。
        return reverse('article:article_detail',args=[self.id,self.slug])

    def get_url_path(self):
        return reverse('article:list_article_detail',args=[self.id,self.slug])