"""
Django settings for learning_log project.

# My settings
# settings.py
#LOGIN_URL = '/users/login/'
LOGIN_URL = 'users:login'
LOGIN_REDIRECT_URL = 'learning_logs:index'  # or your desired redirect

## Settings for django-bootstrap-v5
BOOTSTRAP3 = {
    'include_jquery': False,  # Ensure jQuery is not included
    'javascript_in_head': True,  # Load Bootstrap 5 JavaScript in the head
    'css_url': {
        'href': 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/css/bootstrap.min.css',
        'integrity': 'sha384-whatever-integrity-hash',  # Update with the correct integrity hash from the CDN
        'crossorigin': 'anonymous',
    },
    'javascript_url': {
        'src': 'https://cdn.jsdelivr.net/npm/bootstrap@5.3.0/dist/js/bootstrap.bundle.min.js',
        'integrity': 'sha384-whatever-integrity-hash',  # Update with the correct integrity hash from the CDN
        'crossorigin': 'anonymous',
    },
}



Generated by 'django-admin startproject' using Django 5.1.3.

For more information on this file, see
https://docs.djangoproject.com/en/5.1/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/5.1/ref/settings/
"""

from pathlib import Path

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/5.1/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-eaos3m-d$ipb05l^@h2xoa3hvuo70o*-hu@ha@p3fa49d^1m@b'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS =  ['.onrender.com', 'localhost',
                '127.0.0.1', 'localhost'
                ]
 



# Application definition

INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',

    # Third-party apps
    'bootstrap5',

    # My apps
    'learning_logs',
    'users',

    # other apps
    'widget_tweaks',
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

    # Other middleware...
    'whitenoise.middleware.WhiteNoiseMiddleware',
    # Other middleware...
]

ROOT_URLCONF = 'learning_log.urls'

from django.conf import settings
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [BASE_DIR / "learning_log" / "templates"],  # Points to global templates directory
        'APP_DIRS': True,  # Enables app-specific templates
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


WSGI_APPLICATION = 'learning_log.wsgi.application'


# Database
# https://docs.djangoproject.com/en/5.1/ref/settings/#databases

import os
import dj_database_url  # Make sure this import is correct

# DATABASES Configuration
DATABASES = {
    'default': dj_database_url.config(
        default='postgres://username:password@localhost:5432/dbname'
    )
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/5.1/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/5.1/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/5.1/howto/static-files/

# settings.py
STATIC_URL = '/static/' 
STATIC_ROOT = BASE_DIR / 'staticfiles'   # This is where collected static files will be stored for production
STATICFILES_STORAGE = 'whitenoise.storage.CompressedManifestStaticFilesStorage'
DEBUG = True  # Only for development



# Default primary key field type
# https://docs.djangoproject.com/en/5.1/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'
