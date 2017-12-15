# -*- coding: utf-8 -*-
from django.shortcuts import render
from django.core.paginator import Paginator,EmptyPage,PageNotAnInteger
from .models import ArticleColumn,ArticlePost
from django.shortcuts import get_object_or_404
from django.contrib.auth.decorators import login_required

def article_titles(request):
    articles_title = ArticlePost.objects.all()
    paginator = Paginator(articles_title,5)
    page = request.GET.get('page')
    try:
        current_page = paginator.page(page)
        articles = current_page.object_list
    except PageNotAnInteger:
        current_page = paginator.page(1)
        articles = current_page.object_list
    except EmptyPage:
        current_page = paginator.page(paginator.num_pages)
        articles = current_page.object_list
    return render(request,'article/list/article_titles.html',{'articles':articles,'page':current_page})

#标题超链接
def article_detail(request,id,slug):
    article = get_object_or_404(ArticlePost,id=id,slug=slug)
    return render(request,'article/list/article_detail.html',{'article':article})



