# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from .forms import LoginForm,RegistrationForm,UserProfileForm,UserInfoForm
from django.core.mail import send_mail
# Create your views here.
from django.http import HttpResponse
from django.contrib.auth import authenticate,login #django内置的用户认证和管理应用引入的2个方法
from .forms import LoginForm

from django.contrib.auth.decorators import login_required
from .models import UserProfile,UserInfo
from django.contrib.auth.models import User
from django.core.urlresolvers import reverse

def user_login(request): # 登录视图
    if request.method == 'POST': #
        login_form = LoginForm(request.POST)
        if login_form.is_valid(): # 。验证
            cd = login_form.cleaned_data
            user = authenticate(username=cd['username'],password=cd['password'])

            if user:
                login(request,user)
                return HttpResponse('Welcome you. You have been authenticated successfully')
            else:
                return HttpResponse('Sorry.not right')
        else:
            return HttpResponse('Invaild login')

    if request.method == 'GET':
        login_form = LoginForm()
        return render(request,'account/login.html',{'form':login_form})

def register(request): #注册视图
    if request.method == 'POST':
        user_form = RegistrationForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        #if user_form.is_valid(): #检查的动作
        if user_form.is_valid()*userprofile_form.is_valid():

            new_user = user_form.save(commit=False) #
            new_user.set_password(user_form.cleaned_data['password']) #
            new_user.save()

            new_profile = userprofile_form.save(commit=False)
            new_profile.user = new_user
            new_profile.save()
            UserInfo.objects.create(user=new_user)#用于保存用户注册信息后，同时在account_userinfo数据库表中写入用户的id信息。

            #return HttpResponse('successfully') # 视图函数成功后，会在页面中显示successfully。
            return HttpResponseRedirect(reverse("account:user_login")) # 160:视图函数成功后，跳转到登录界面。

        else:
            return HttpResponse('sorry,your can not register.')
    else:
        user_form = RegistrationForm()
        userprofile_form = UserProfileForm()
        return render(request,'account/register.html',{'form':user_form,'profile':userprofile_form})

#展示个人信息的视图函数views
@login_required(login_url='/account/login/') #引入装饰器，将没有登录的用户转到登录界面
def myself(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=user)
    userinfo = UserInfo.objects.get(user=user)
    return render(request,'account/myself.html',{'user':user,'userprofile':userprofile,'userinfo':userinfo})

#编辑个人信息p93
from django.http import HttpResponseRedirect # 引入Http，用于实现URL跳转，
from .forms import UserProfileForm,UserInfoForm,UserForm

@login_required(login_url='/account/login/')
def myself_edit(request):
    user = User.objects.get(username=request.user.username)
    userprofile = UserProfile.objects.get(user=request.user)
    userinfo=UserInfo.objects.get(user=request.user)

    if request.method == 'POST':
        user_form = UserForm(request.POST)
        userprofile_form = UserProfileForm(request.POST)
        userinfo_form = UserInfoForm(request.POST)
        if user_form.is_valid()*userprofile_form.is_valid()*userinfo_form.is_valid():
            user_cd = user_form.cleaned_data
            userprofile_cd = userprofile_form.cleaned_data
            userinfo_cd = userinfo_form.cleaned_data
            print(user_cd['email'])
            user.email = user_cd['email']
            userprofile.birth = userprofile_cd['birth']
            userprofile.phone = userprofile_cd['phone']
            userinfo.school = userinfo_cd['school']
            userinfo.company = userinfo_cd['company']
            userinfo.profession = userinfo_cd['profession']
            userinfo.address = userinfo_cd['address']
            userinfo.aboutme = userinfo_cd['aboutme']
            user.save()
            userprofile.save()
            userinfo.save()
        return HttpResponseRedirect('/account/my-information/') # 当用户提交个人信息并通过后端验证保存之后，执行本句，跳转到my-information，查看自己修改结果
    else:
        user_form = UserForm(instance=request.user)
        userprofile_form=UserProfileForm(initial={'birth':userprofile.birth,'phone':userprofile.phone})
        userinfo_form = UserInfoForm(initial={'school':userinfo.school,'company':userinfo.company,'profession':userinfo.profession,'address':userinfo.address,'aboutme':userinfo.aboutme})
        return render(request,'account/myself_edit.html',{'user_form':user_form,'userprofile_form':userprofile_form,'userinfo_form':userinfo_form})

#图片上传，实现存储前端传过来的图片
@login_required(login_url='/account/login/')
def my_image(request):
    if request.method == 'POST':
        img =request.POST['img'] # 得到前端以post方式提交打图片，已经规定提交的字典数据中有img这个键
        userinfo = UserInfo.objects.get(user=request.user.id)
        userinfo.photo = img
        userinfo.save()
        return HttpResponse('1')
    else:
        return render(request,'account/imagecrop.html',)