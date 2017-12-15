# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from .models import UserProfile,UserInfo

# Register your models here.

class UserProfileAdmin(admin.ModelAdmin):
    list_display = ('user','birth','phone',)#列出列表中的项目。
    list_filter =('phone',) #规定网页右边filter的显示内容，根据电话过滤显示列表

admin.site.register(UserProfile,UserProfileAdmin)

class UserInfoAdmin(admin.ModelAdmin):
    list_display = ('user','school', 'company', 'profession', 'address','aboutme','photo')  # 列出列表中的项目。
    list_filter = ('school', 'company', 'profession')  # 规定网页右边filter的显示内容，根据电话过滤显示列表


admin.site.register(UserInfo, UserInfoAdmin)