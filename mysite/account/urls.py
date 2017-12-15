# -*- coding: utf-8 -*-
from django.conf.urls import url
from . import views

from django.conf import settings

from django.contrib.auth import views as auth_views #引入django内置的视图文件，重命名为auth-views

urlpatterns =[
    #url(r'^login/$', views.user_login, name='user_login'),#自定义打登录
    url(r'^login/$', auth_views.login, name='user_login'), #django内置的登录
    url(r'^new-login/$',auth_views.login,{'template_name':'account/login.html'}),
    url(r'^logout/$', auth_views.logout, name='user_logout'), #django内置的退出
    #url(r'^logout/$', auth_views.logout,{'template_name':'account/logout.html'}, name='user_logout'), #django内置的退出
    url(r'^register/$',views.register,name='user_register'),

    # 登陆密码修改的链接
    url(r'^password-change/$',auth_views.password_change,{'post_change_redirect':'/account/password-change-done'},name='password_change'),
    url(r'^password-change-done/$',auth_views.password_change_done,name='password_change_done'),

    # 登录密码重置链接(自定义)
    url(r'^password-reset/$',auth_views.password_reset,
        {'template_name':'account/password_reset_form.html',
        'email_template_name':'account/password_reset_email.html',
         'subject_template_name':'account/password_reset_subject.text',
         'post_reset_redirect':'/account/password-reset-done'
         },name='password_reset'),
    url(r'^password-reset-done/$',auth_views.password_reset_done,
        {'template_name':'account/password_reset_done.html',
         },name='password_reset_done'),
    url(r'^password-reset_confirm/(?P<uidb64>[-\w]+)/(?P<token>[-\w]+)/$',auth_views.password_reset_confirm,
        {'template_name':'account/password_reset_confirm.html',
         'post_reset_redirect':'/account/password-reset-complete'
         },name='password_reset_confirm'),
    url(r'^password-reset_complete/$',auth_views.password_reset_complete,
        {'template_name':'account/password_reset_complete.html',
         },name='password_reset_complete'),

    #个人信息设置路径
    url(r'^my-information/$',views.myself,name='my_information'),
    url(r'^edit-my-information/$',views.myself_edit,name='edit_my_information'),
    url(r'^my-image/$', views.my_image,name='my_image'),
]