# -*- coding: utf-8 -*-
"""
Django settings for web_manage project.

For more information on this file, see
https://docs.djangoproject.com/en/1.7/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.7/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.7/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '%3t=*yk(*_)@i@#o!f@1w!a0!76q(a3s2zh53&mj*==f=7lqz9'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    #'grappelli.dashboard',
    #'grappelli',
    'suit',
    'django.contrib.admin',
    'django.contrib.admindocs',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'cheats',
    'signatures',
    'games',
)

MIDDLEWARE_CLASSES = (
    #'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    #'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.locale.LocaleMiddleware',  
    'django.middleware.common.CommonMiddleware',
    #'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'pagination.middleware.PaginationMiddleware',
)


TEMPLATE_CONTEXT_PROCESSORS = (
    'django.contrib.auth.context_processors.auth',
    'django.core.context_processors.debug',
    'django.core.context_processors.i18n',
    'django.core.context_processors.media',
    'django.core.context_processors.request',
    "django.core.context_processors.static",
    "django.core.context_processors.tz",
    "django.contrib.messages.context_processors.messages"
)

SUIT_CONFIG = {
    # header
    'ADMIN_NAME': u'*****',
    
    #'LIST_PER_PAGE': 10,
    'MENU': (
        {'label': u'作弊页面管理', 'icon':'icon-leaf', 'app': 'cheats'},
        {'label': u'特征码管理', 'icon':'icon-barcode', 'app': 'signatures'},
        {'label': u'游戏管理', 'icon':'icon-plane', 'app': 'games'},
        {'label': u'用户管理', 'app': 'auth'},
             ),
}

#AUTH_USER_MODEL = 'app.User'

ROOT_URLCONF = 'WebManage.urls'

WSGI_APPLICATION = 'WebManage.wsgi.application'


# Database
# https://docs.djangoproject.com/en/1.7/ref/settings/#databases

DATABASES ={
    'default': {
        'ENGINE': 'sqlserver',
        'NAME': '*****',
        'HOST': '*****',
        'PORT': '1433',
        'USER': '*****',
        'PASSWORD': '*****',
        'OPTIONS': {
            'DRIVER': 'SQL Server Native Client 10.0',
        },
    }
}
DATABASE_OPTIONS = {  
        'host_is_server': False,  
        'dsn': 'MSSQL-PYTHON',  
}



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
# https://docs.djangoproject.com/en/1.7/topics/i18n/

LANGUAGE_CODE = 'zh_CN'

#TIME_ZONE = 'UTC'
TIME_ZONE = 'Asia/Shanghai'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.7/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = (
    os.path.join(BASE_DIR, 'static/'),
#    '/var/www/static',
    
)

