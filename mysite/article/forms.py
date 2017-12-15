# -*- coding: utf-8 -*-
from django import forms
from .models import ArticleColumn,ArticlePost

#在拥有数据模型的情况下，创建表单，因为需要通过表单填写栏目名称，为column字段赋值
class ArticleColumnForm(forms.ModelForm):
    class Meta:
        model = ArticleColumn
        fields = ('column',)

#文章发布表单
class ArticlePostForm(forms.ModelForm):
    class Meta:
        model = ArticlePost
        fields = ('title','body')