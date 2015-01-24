
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))


SECRET_KEY = '111'

DEBUG = True

TEMPLATE_DEBUG = True

ALLOWED_HOSTS = []


INSTALLED_APPS = (
    'django_slack',
)

MIDDLEWARE_CLASSES = (
    'django.middleware.common.CommonMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
)

ROOT_URLCONF = 'django_slack_test.urls'

WSGI_APPLICATION = 'django_slack_test.wsgi.application'

