"""
Django settings for ResumeColab project.

Generated by 'django-admin startproject' using Django 3.0.8.

For more information on this file, see
https://docs.djangoproject.com/en/3.0/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.0/ref/settings/
"""

import os
import dj_database_url

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.0/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '3ex%y#wib@9p&*q*g$u&&1qy6u2%^&&j%@70!q$w-9qj9fosc^'
# SECRET_KEY = os.environ.get('SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = False

ALLOWED_HOSTS = ['makerspace-colab.herokuapp.com', '127.0.0.1']


# Application definition

INSTALLED_APPS = [
    'account_profile',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'whitenoise.middleware.WhiteNoiseMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'ResumeColab.middleware.LoginRequiredMiddleware',
]

ROOT_URLCONF = 'ResumeColab.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
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

WSGI_APPLICATION = 'ResumeColab.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.0/ref/settings/#databases

DATABASES = {
        'default': {
            'ENGINE': 'django.db.backends.postgresql',
            #'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
            'NAME': 'ddjcielcpnn28b',
            'USER': 'szdfhkccuuzcud',
            'PASSWORD': '7084994a304abf9c75f73ae34023195bba83b4ff53e9d4abd8ce3c333d33a884',
            'HOST': 'ec2-54-197-254-117.compute-1.amazonaws.com',
            'PORT': '5432',
        }
}

# db_from_env = dj_database_url.config(conn_max_age=600)
# DATABASES['default'].update(db_from_env)


# Password validation
# https://docs.djangoproject.com/en/3.0/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.0/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.0/howto/static-files/

STATIC_URL = '/static/'

#location where django collect all static files
STATIC_ROOT = os.path.join(BASE_DIR,'staticfiles')

# location where you will store your static files
# STATICFILES_DIRS = [os.path.join(BASE_DIR,'ResumeColab/static')]

# MEDIA_ROOT = os.path.join(BASE_DIR,'media')
# MEDIA_URL = '/media/'


LOGIN_REDIRECT_URL = '/'

LOGIN_URL = '/login/'

LOGIN_EXEMPT_URLS = {
    'home/',
    'logout/',
    'register/',
    'password_reset/done/',
    'reset/',
    'password_reset/',
    # 'reset/done/',
}

# EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'  # During development only
# EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_USE_TLS = True
# EMAIL_PORT = 587
# EMAIL_HOST_USER = 'makerspace.colab@gmail.com'
# EMAIL_HOST_PASSWORD = 'MakerspaceColab@93'


# STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
