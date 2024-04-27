import os
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# Load environment variables from .env file
ENV_FILE_PATH = BASE_DIR / ".env_base"
load_dotenv(str(ENV_FILE_PATH))

# Django secret key
DJANGO_SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# Email setups
EMAIL_HOST = os.environ.get('EMAIL_HOST')
EMAIL_PORT = os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER = os.environ.get('EMAIL_HOST_USER')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL = os.environ.get('DEFAULT_FROM_EMAIL')
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')
EMAIL_USE_TLS = os.environ.get('EMAIL_USE_TLS')
EMAIL_USE_SSL = os.environ.get('EMAIL_USE_SSL')

# Debug mode and allowed hosts
DEBUG = os.environ.get('DEBUG')
ALLOWED_HOSTS = os.environ.get('ALLOWED_HOSTS', '').split(',')

# Application definition
INSTALLED_APPS = [
    app.strip() for app in os.environ.get('INSTALLED_APPS', '').split(',')
]

MIDDLEWARE = [
    middleware.strip() for middleware in os.environ.get('MIDDLEWARE', '').split(',')
]

ROOT_URLCONF = os.environ.get('ROOT_URLCONF')
WAGTAILADMIN_BASE_URL = os.environ.get('WAGTAILADMIN_BASE_URL')

# WAGTAIL SETUPS
WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': os.environ.get('WAGTAILSEARCH_BACKEND'),
    }
}

WAGTAIL_SITE_NAME = os.environ.get('WAGTAIL_SITE_NAME')

# RESTFRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
        'rest_framework.permissions.' + permission.strip()
        for permission in os.environ.get('DEFAULT_PERMISSION_CLASSES', '').split(',')
    ]
}

# Redis Setup
REDIS_HOST = os.environ.get('REDIS_HOST')
REDIS_PORT = os.environ.get('REDIS_PORT')
REDIS_DB = os.environ.get('REDIS_DB')

# DJANGO ADMIN SETUPS
LOGIN_URL = os.environ.get('LOGIN_URL')
LOGOUT_URL = os.environ.get('LOGOUT_URL')

# WEBAPP SETTINGS
EMAIL_BACKEND = os.environ.get('EMAIL_BACKEND')

# Ecommerce App
CART_SESSION_ID = os.environ.get('CART_SESSION_ID')

# BRAINTREE SETUP
BRAINTREE_MERCHANT_ID = os.environ.get('BRAINTREE_MERCHANT_ID')
BRAINTREE_PUBLIC_KEY = os.environ.get('BRAINTREE_PUBLIC_KEY')
BRAINTREE_PRIVATE_KEY = os.environ.get('BRAINTREE_PRIVATE_KEY')

# Celery setup
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
CELERY_ACCEPT_CONTENT = os.environ.get('CELERY_ACCEPT_CONTENT')
CELERY_RESULT_SERIALIZER = os.environ.get('CELERY_RESULT_SERIALIZER')
CELERY_TASK_SERIALIZER = os.environ.get('CELERY_TASK_SERIALIZER')

# Authentication backends
AUTHENTICATION_BACKENDS = [
    backend.strip() for backend in os.environ.get('AUTHENTICATION_BACKENDS', '').split(',')
]

# Social auth settings
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_FACEBOOK_SCOPE = os.environ.get('SOCIAL_AUTH_FACEBOOK_SCOPE', '').split(',')

SOCIAL_AUTH_TWITTER_KEY = os.environ.get('SOCIAL_AUTH_TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET = os.environ.get('SOCIAL_AUTH_TWITTER_SECRET')

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET')

# Templates configuration
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, 'templates')), ],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                processor.strip()
                for processor in os.environ.get('TEMPLATES_CONTEXT_PROCESSORS', '').split(',')
            ],
        },
    },
]

# Internationalization settings
LANGUAGE_CODE = os.environ.get('LANGUAGE_CODE')
TIME_ZONE = os.environ.get('TIME_ZONE')
USE_I18N = os.environ.get('USE_I18N')
USE_L10N = os.environ.get('USE_L10N')
USE_TZ = os.environ.get('USE_TZ')

# Static files (CSS, JavaScript, Images)
STATIC_URL = os.environ.get('STATIC_URL')
STATIC_ROOT = os.environ.get('STATIC_ROOT')
MEDIA_URL = os.environ.get('MEDIA_URL')
MEDIA_ROOT = os.environ.get('MEDIA_ROOT')
