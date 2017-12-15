# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models

# Create your models here.  p13
from django.utils import timezone
from django.contrib.auth.models import User

import sys
reload(sys)
sys.setdefaultencoding('utf8') # 没有这三句无法输入汉字打 title

class BlogArticles(models.Model):
    title = models.CharField(max_length=300)
    author = models.ForeignKey(User,related_name='blog_posts')
    body = models.TextField()
    publish = models.DateTimeField(default=timezone.now)

    class Meta:
        ordering = ('-publish',)

    def __str__(self):
        return self.title