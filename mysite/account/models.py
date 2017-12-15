# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django.contrib.auth.models import User

# Create your models here.

class UserProfile(models.Model):#定义数据模型类对应着要在数据库中建立名为account_userprofile的数据库表。
    user = models.OneToOneField(User,unique=True) # 含义是通过user这个字段（作为纽带），声明UserProfile类与User类之间打关系是‘一对一’。
    birth = models.DateField(blank=True,null=True)
    phone = models.CharField(max_length=20,null=True)

    def __str__(self):
        return 'user{}'.format(self.user.username)

#个人信息维护
class UserInfo(models.Model):
    user = models.OneToOneField(User,unique=True)
    school = models.CharField(max_length=100,blank=True)
    company = models.CharField(max_length=100,blank=True)
    profession = models.CharField(max_length=100,blank=True)
    address = models.CharField(max_length=100,blank=True)
    aboutme = models.TextField(blank=True)
    photo = models.ImageField(blank=True)

    def __str__(self):
        return 'user{}'.format(self.user.username)