"""
Django settings for IMnight project.

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
SECRET_KEY = 'ti#_4flcu1o_%!)rxqvujigi5=1=kl!9k9f(m^r1-+q8m+v*ub'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = []


# Application definition

INSTALLED_APPS = [
    'channels',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # django REST framework
    # http://www.django-rest-framework.org
    'rest_framework',
    'rest_framework.authtoken',

    'rest_framework_swagger',

    # http://django-rest-auth.readthedocs.io/en/latest/index.html
    'django.contrib.sites',
    'allauth',
    'allauth.account',

    'allauth.socialaccount',
    'allauth.socialaccount.providers.facebook',

    # self create apps
    'accounts',
    'human',
    'earth',
    'lottery',
]

SITE_ID = 1

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
]

ROOT_URLCONF = 'IMnight.urls'

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

WSGI_APPLICATION = 'IMnight.wsgi.application'


# Database

# DATABASES = {
#     'default': {
#         'ENGINE': 'django.db.backends.sqlite3',
#         'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
#     }
# }

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'imnight_backend',
        'USER': 'django',
        'PASSWORD': 'bnjaAKWULde^22=9$!fq',
        'HOST': '140.112.106.45',
        'PORT': '5432',
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

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True

# django REST framework
# http://www.django-rest-framework.org

REST_FRAMEWORK = {

}

EMAIL_BACKEND = 'django.core.mail.backends.smtp.EmailBackend'
# TLS Port
EMAIL_PORT = 587
EMAIL_USE_TLS = True
EMAIL_HOST = 'smtp.gmail.com'
# EMAIL_HOST_USER = ''
# Application Key
# EMAIL_HOST_PASSWORD = ''


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/1.11/howto/static-files/

STATIC_URL = '/static/'

# Channel for chat
# https://blog.heroku.com/in_deep_with_django_channels_the_future_of_real_time_apps_in_django
redis_host = os.environ.get('REDIS_HOST', 'localhost')

CHANNEL_LAYERS = {
    "default": {
        "BACKEND": "asgi_redis.RedisChannelLayer",
        "CONFIG": {
            "hosts": [os.environ.get('REDIS_URL', 'redis://localhost:6379')],
        },
        "ROUTING": "human.chat.routing.channel_routing",
    },
}

# Logger
# https://www.webforefront.com/django/setupdjangologging.html
LOGGING = {
    'version': 1,
    'disable_existing_loggers': False,
    'formatters': {
        'verbose': {
            'format': '%(levelname)s - [%(asctime)s] (%(module)s %(process)d %(thread)d) %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
        'simple': {
            'format': '%(levelname)s - [%(asctime)s] %(message)s',
            'datefmt': '%Y-%m-%d %H:%M:%S'
        },
    },
    'handlers': {
        'console': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.StreamHandler',
            'formatter': 'simple'
        },
        'development_logfile': {
            'level': 'DEBUG',
            'filters': ['require_debug_true'],
            'class': 'logging.FileHandler',
            'filename': 'tmp/django_dev.log',
            'formatter': 'verbose'
        },
        'production_logfile': {
            'level': 'ERROR',
            'filters': ['require_debug_false'],
            'class': 'logging.handlers.RotatingFileHandler',
            'filename': 'tmp/django_production.log',
            'maxBytes': 1024 * 1024 * 100,  # 100MB
            'backupCount': 5,
            'formatter': 'simple'
        },
        'dba_logfile': {
            'level': 'DEBUG',
            'filters': ['require_debug_false', 'require_debug_true'],
            'class': 'logging.handlers.WatchedFileHandler',
            'filename': 'tmp/django_dba.log',
            'formatter': 'simple'
        },
    },
    'loggers': {
        'testdevelop': {
            'handlers': ['console', ],
        },
        'coffeehouse': {
            'handlers': ['development_logfile', 'production_logfile'],
        },
        'dba': {
            'handlers': ['dba_logfile'],
        },
        'django': {
            'handlers': ['development_logfile', 'production_logfile'],
        },
        'py.warnings': {
            'handlers': ['development_logfile'],
        },
    },
    'filters': {
        'require_debug_false': {
            '()': 'django.utils.log.RequireDebugFalse',
        },
        'require_debug_true': {
            '()': 'django.utils.log.RequireDebugTrue',
        },
    },
}
