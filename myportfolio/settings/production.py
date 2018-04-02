import os 
import dj_database_url
from .base import *

DEBUG = False
TEMPLATE_DEBUG = False
SECRET_KEY = os.environ.get('SECRET_KEY')

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            os.path.join(BASE_DIR, 'templates')
        ],
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

DATABASES = {
	'default': dj_database_url.config(
		default='sqlite:///{}'.format(
				os.path.abspath(os.path.join(BASE_DIR, 'db.sqlite3'))),
		),
}

ALLOWED_HOSTS = ['*']
SECURE_PROXY_SSL_HEADER = ('HTTP_X_FORWARDED_PROTO', 'https')
MEDIA_URL = '/media/'

MEDIA_ROOT = os.path.join(BASE_DIR, 'baseapp/media')
