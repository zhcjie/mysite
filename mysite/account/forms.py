# -*- coding: utf-8 -*-
from django import forms
from django.contrib.auth.models import User #引入django默认用户类型user类
from django.db import models
from .models import UserProfile,UserInfo

#登录表单
class LoginForm(forms.Form): #需要对表单的数据增删改查用ModelForm，只用于提交不修改数据用Model。
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput) #密码输入

#注册表单
class RegistrationForm(forms.ModelForm):
    password=forms.CharField(label='Password',widget=forms.PasswordInput)
    password2=forms.CharField(label='Confirm Password',widget=forms.PasswordInput)

    class Meta:  #内部类，需要声明本表单所应用的数据类型。
        model = User  # 就是表单的内容会写入哪个数据库表中的哪些记录里
        fields = ('username','email') #说明所选用的属性。或用exclude列表说明排除的属性
        #fields = '__all__'

    def clean_password2(self): #检验用户输入两次密码是否一致
        cd =self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('password do not match.')
        return cd['password2']

#新增注册表单的内容
class UserProfileForm(forms.ModelForm):
    class Meta:
        model = UserProfile
        fields = ('phone','birth',)

#个人信息维护表单
class UserInfoForm(forms.ModelForm):
    class Meta:
        model = UserInfo
        fields = ('school','company','profession','address','aboutme','photo')

class UserForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('email',)
