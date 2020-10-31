# coding: utf-8
import os
from decouple import config
from unipath import Path
import dj_database_url

BASE_DIR = Path(__file__).parent
ROOT_DIR = Path(__file__).ancestor(2)

DEBUG = config('DEBUG', default=False, cast=bool)
SECRET_KEY = config('SECRET_KEY')

ALLOWED_HOSTS = [
    'localhost',
    '127.0.0.1',
    'gastosluxu.herokuapp.com'
]

INSTALLED_APPS = [
    # General use templates & template tags (should appear first)
    'django_adminlte',
    # Optional: Django admin theme (must be before django.contrib.admin)
    # 'django_adminlte_theme',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    # lib
    'debug_toolbar',
    'widget_tweaks',
    'django_extensions',
    'django_select2',
    'django_ajax',
    # Third-party
    'crispy_forms',
    'dynamic_formsets',
    'cruds_adminlte',
    # 'table',
    # apps
    'accounts',
    'website'
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'debug_toolbar.middleware.DebugToolbarMiddleware',
]

ROOT_URLCONF = 'urban_train.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': ['templates'],
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

WSGI_APPLICATION = 'urban_train.wsgi.application'

# Database
# https://docs.djangoproject.com/en/1.10/ref/settings/#databases
DATABASES = {}
DATABASES['default'] = dj_database_url.config(
    conn_max_age=600,
    ssl_require=True,
    default=config('DATABASE_URL')
)
DATABASES['default']['ATOMIC_REQUESTS'] = True


# Password validation
# https://docs.djangoproject.com/en/1.10/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/1.10/topics/i18n/

LANGUAGE_CODE = 'pt-br'
TIME_ZONE = 'America/Sao_Paulo'
USE_I18N = True
USE_L10N = True
USE_TZ = True
LOCALE_PATHS = [BASE_DIR, "locale"]
# https://docs.djangoproject.com/en/dev/ref/settings/#locale-paths

# STATIC
STATIC_URL = "/static/"
STATIC_ROOT = os.path.join(ROOT_DIR, "staticfiles")
STATICFILES_DIRS = [
    os.path.join(ROOT_DIR, "static")
]

# https://docs.djangoproject.com/en/dev/ref/contrib/staticfiles/#staticfiles-finders
STATICFILES_FINDERS = [
    "django.contrib.staticfiles.finders.FileSystemFinder",
    "django.contrib.staticfiles.finders.AppDirectoriesFinder",
]

MEDIA_URL = "/django-summernote/"
MEDIA_ROOT = os.path.join(BASE_DIR, 'media/')

CRISPY_TEMPLATE_PACK = 'bootstrap4'

# auth
LOGIN_URL = '/entrar/'
AUTH_USER_MODEL = 'accounts.User'
AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'accounts.backends.ModelBackend',
)

INTERNAL_IPS = [
    # ...
    '127.0.0.1',
    # ...
]

# CACHES
# ------------------------------------------------------------------------------
# https://docs.djangoproject.com/en/dev/ref/settings/#caches
CACHES = {
    "default": {
        "BACKEND": "django.core.cache.backends.locmem.LocMemCache",
        "LOCATION": "",
    }
}

# MEDIA_URL = "/django-summernote/"
# MEDIA_ROOT = os.path.join(BASE_DIR, "media/")

SUMMERNOTE_CONFIG = {
    'summernote': {
        # As an example, using Summernote Air-mode
        'airMode': False,
        'lang': 'pt-BR',
    }
}
