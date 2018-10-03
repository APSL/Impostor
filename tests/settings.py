# -*- encoding: utf-8 -*-

import os

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR, 'db.sqlite3'),
    }
}

INSTALLED_APPS = [
    'django.contrib.contenttypes',
    'django.contrib.staticfiles',
    'django.contrib.auth',
    'impostor',
    'tests'
]

MIDDLEWARE_CLASSES = MIDDLEWARE = []

USE_TZ = True

SECRET_KEY = 'foobar'

LANGUAGE_CODE = 'en-us'

TEMPLATES = [{
    'BACKEND': 'django.template.backends.django.DjangoTemplates',
    'APP_DIRS': True,
}]


STATIC_URL = '/static/'

ANONYMIZE_ENABLED = True

AUTHENTICATION_BACKENDS = (
    'django.contrib.auth.backends.ModelBackend',
    'impostor.backend.AuthBackend',
)
