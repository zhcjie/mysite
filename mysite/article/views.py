# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger

# Create your views here.
from django.contrib.auth.decorators import login_required
from django.views.decorators.csrf import csrf_exempt
from django.http import HttpResponse
from .models import ArticleColumn,ArticlePost
from .forms import ArticleColumnForm,ArticlePostForm
from django.views.decorators.http import require_POST
from django.shortcuts import get_object_or_404

@login_required(login_url='/account/login/')
def article_column(request):
    columns = ArticleColumn.objects.filter(user=request.user)#将数据库表中该用户所属的栏目都读取出来。
    return render(request,'article/column/article_column.html',{'columns':columns})

# 创建一个新栏目
@login_required(login_url='/account/login/')
@csrf_exempt  #提交表单csrf问题，可以添加装饰器
def article_column(request):
    if request.method == 'GET':
        column = ArticleColumn.objects.filter(user=request.user)
        column_form = ArticleColumnForm()
        return render(request,'article/column/article_column.html',{'column':column,'column_form':column_form})

    if request.method == 'POST':
        column_name = request.POST['column']
        columns = ArticleColumn.objects.filter(user_id=request.user.id,column=column_name)
        if columns: # 创建条件为:1.当前用户,2.是否存在该栏目。
            return HttpResponse('2')
        else:       # 如果不存在就可以创建
            ArticleColumn.objects.create(user=request.user,column=column_name)
            return HttpResponse('1')

# 编辑栏目
@login_required(login_url='/account/login/')
@require_POST #保证只能接受通过POST方式提交数据。
@csrf_exempt  #提交表单csrf问题，可以添加装饰器。
def rename_article_column(request):
    column_name = request.POST["column_name"]
    column_id = request.POST["column_id"]
    try:
        line = ArticleColumn.objects.get(id=column_id)
        line.column = column_name
        line.save()
        return HttpResponse("1")
    except:
        return HttpResponse("0")

# 删除栏目
@login_required(login_url='/account/login/')
@require_POST #保证只能接受通过POST方式提交数据。
@csrf_exempt  #提交表单csrf问题，可以添加装饰器。
def del_article_column(request):
    column_id = request.POST["column_id"]
    try:
        line = ArticleColumn.objects.get(id=column_id)
        line.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")

# 文章发布视图
@login_required(login_url='/account/login/')
@csrf_exempt  #提交表单csrf问题，可以添加装饰器。
def article_post(request):
    if request.method=='POST':
        article_post_form = ArticlePostForm(data=request.POST)
        if article_post_form.is_valid():
            cd = article_post_form.cleaned_data
            try:
                new_article = article_post_form.save(commit=False)
                new_article.author = request.user
                new_article.column = request.user.article_column.get(id=request.POST['column_id'])
                new_article.save()
                return HttpResponse('1')
            except:
                return HttpResponse('2')
        else:
            return HttpResponse('3')
    else:
        article_post_form=ArticlePostForm()
        article_columns=request.user.article_column.all() # 128查看如何运转
        return render(request,'article/column/article_post.html',{'article_post_form':article_post_form,'article_columns':article_columns})

#文章发布后显示，标题列表,  分页功能(p147)
@login_required(login_url='/account/login')
def article_list(request):
    articles_list = ArticlePost.objects.filter(author=request.user)#筛选出用户的所有文章对象，并将对象渲染到模板。
    paginator = Paginator(articles_list,5)#根据查询到的文章对象创建分页实例对象,规定每页最多2个
    page = request.GET.get('page')# 获得当前浏览器get请求的参数page的值,
    try:
        current_page = paginator.page(page)#page()是Paginator对象的一个方法,用来获得指定页面内容.
        articles = current_page.object_list#object_list是Page对象的属性,获得该页所有对象列表.
    except PageNotAnInteger:#捕获异常,页码不是整数
        current_page = paginator.page(1)
        articles =current_page.object_list
    except EmptyPage:#异常,页码为空
        current_page = paginator.page(paginator.num_pages)#返回页数,num_pages是paginator的属性.
        articles =current_page.object_list
    return render(request,'article/column/article_list.html',{'articles':articles,'page':current_page})



#标题超链接
@login_required(login_url='/account/login')
def article_detail(request,id,slug):
    article = get_object_or_404(ArticlePost,id=id,slug=slug)
    return render(request,'article/column/article_detail.html',{'article':article})

#删除文章p142
@login_required(login_url='/account/login')
@require_POST
@csrf_exempt
def del_article(request):
    article_id = request.POST['article_id']
    try:
        article = ArticlePost.objects.get(id=article_id)
        article.delete()
        return HttpResponse("1")
    except:
        return HttpResponse("2")

#修改文章内容
@login_required(login_url='/account/login')
@csrf_exempt
def redit_article(request,article_id):
    if request.method == 'GET':
        article_columns = request.user.article_column.all()
        article = ArticlePost.objects.get(id=article_id)
        this_article_form = ArticlePostForm(initial={'title':article.title})
        this_article_column = article.column
        return render(request,'article/column/redit_article.html',{'article':article,'article_columns':article_column,'this_article_column':this_article_column,'this_article_form':this_article_form})
    else:
        redit_article = ArticlePost.objects.get(id=article_id)
        try:
            redit_article.column = request.user.article_column.get(id=request.POST['column_id'])
            redit_article.title = request.POST['title']
            redit_article.body = request.POST['body']
            redit_article.save()
            return HttpResponse("1")
        except:
            return HttpResponse("2")