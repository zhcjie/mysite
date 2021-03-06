# -*- coding: utf-8 -*-
"""
Django settings for mysite project.

Generated by 'django-admin startproject' using Django 1.11.5.

For more information on this file, see
https://docs.djangoproject.com/en/1.11/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.11/ref/settings/
"""

import os

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.11/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'jolc^#=-8e4z8@=ekmek2(h(x500@14xe99pn_@)=l$msjs&#6'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True
#开发模式  False为生产模式

ALLOWED_HOSTS = []
#主域名


# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'blog',
    'account',
    'password_reset',
    'article',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',

]

ROOT_URLCONF = 'mysite.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR,'templates')],
        'APP_DIRS': False,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'mysite.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.11/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}


# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]


# Internationalization
# https://docs.djangoproject.com/en/1.11/topics/i18n/

#LANGUAGE_CODE = 'en-us'
LANGUAGE_CODE = 'zh-hans'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR,'static'),
)

LOGIN_REDIRECT_URL = '/home/' #登录重定向，老齐 p58

#p82 配置邮件发送服务器

EMAIL_HOST = 'smtp.qq.com'
EMAIL_HOST_USER = 'your_account@qq.com'
EMAIL_HOST_PASSWORD = 'your_account@qq.com'
EMAIL_POST = 465
EMAIL_USE_TLS =True
DEFAULT_FROM_EMAIL = 'your_account@qq.com'

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

# send e-mail
#EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'  #email后端
#EMAIL_USE_TLS = False   #是否使用TLS安全传输协议
#EMAIL_USE_SSL = True    #是否使用SSL加密，qq企业邮箱要求使用
#EMAIL_HOST = 'smtp.qq.com'   #发送邮件的邮箱 的 SMTP服务器(smtp.exmail.qq.com)，这里用了qq企业邮箱
#EMAIL_PORT = 465     #发件箱的SMTP服务器端口
#EMAIL_HOST_USER = '422235116@qq.com'    #发送邮件的邮箱地址
#EMAIL_HOST_PASSWORD = 'blogblog'         #发送邮件的邮箱密码

#from django.core.mail import send_mail   存在错误（环境配置问题）
#send_mail('learn','nihao','your_account@qq.com',['2270859952@qq.com'],fail_silently=False)