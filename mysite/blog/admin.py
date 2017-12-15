# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

# Register your models here.
from .models import BlogArticles
#admin.site.register(BlogArticles)

class BlogArticlesAdmin(admin.ModelAdmin):

    list_display = ('title','author','publish')# 表头
    list_filter = ('publish','author') # 过滤器
    search_fields = ('title','body') # 搜索栏
    raw_id_fields = ('author',)
    date_hierarchy = 'publish'
    ordering = ['publish','author']

admin.site.register(BlogArticles,BlogArticlesAdmin)