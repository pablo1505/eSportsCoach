"""
Django settings for esport_tutor project.

Generated by 'django-admin startproject' using Django 1.8.6.

For more information on this file, see
https://docs.djangoproject.com/en/1.8/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/1.8/ref/settings/
"""

# Build paths inside the project like this: os.path.join(BASE_DIR, ...)
import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/1.8/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'wd+rx85m%8x%dpp9r-e-@swp6$b6kg0pe(=c@coy#6r7qa5(oc'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = (
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'sideapp',
)

MIDDLEWARE_CLASSES = (
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.auth.middleware.SessionAuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.middleware.security.SecurityMiddleware',
)

ROOT_URLCONF = 'esport_coach.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [os.path.join(BASE_DIR, "templates")],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.core.context_processors.static',
            ],
        },
    },
]

WSGI_APPLICATION = 'esport_coach.wsgi.application'

EMAIL_HOST = 'smtp.gmail.com'
EMAIL_HOST_USER = 'esportcoach@gmail.com'
EMAIL_HOST_PASSWORD = 'Esportcoach1234!'
EMAIL_PORT = 587
EMAIL_USE_TLS = True



# Database
# https://docs.djangoproject.com/en/1.8/ref/settings/#databases

# DATABASES = {
#         'default': {
#             'ENGINE': 'django.db.backends.postgresql_psycopg2', # Add 'postgresql_psycopg2', 'mysql', 'sqlite3' or 'oracle'.
#             'NAME': 'coachbase',                      # Or path to database file if using sqlite3.
#             # The following settings are not used with sqlite3:
#             'USER': 'feiyu',
#             'PASSWORD': 'abc1234',
#             'HOST': 'localhost',                      # Empty for localhost through domain sockets or           '127.0.0.1' for localhost through TCP.
#             'PORT': '5432',                      # Set to empty string for default.
#         }
#     }

"""
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'etutor',
        'USER': 'postgres',
        'PASSWORD': 'Pablocpe2',
        'HOST': '127.0.0.1',
        'PORT': '5432',
    }
}
"""


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'd6ev70m5pvg0gd',
        'USER': 'zawbmqgrzewebr',
        'PASSWORD': 'w0ens6pGX3k52WVxl6NsyXn5Ea',
        'HOST': 'ec2-54-83-199-54.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}


# Internationalization
# https://docs.djangoproject.com/en/1.8/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.8/howto/static-files/

STATIC_URL = '/static/'

STATIC_ROOT = os.path.join(BASE_DIR, "static", 'static_root')

STATICFILES_DIRS = (
    os.path.join(BASE_DIR, "static", 'sub_static'),
    )

MEDIA_URL = '/media/'
MEDIA_ROOT = os.path.join(BASE_DIR, "static", 'media_root')
