

import os
import environ
from pathlib import Path
from dotenv import load_dotenv

# Build paths inside the project like this: BASE_DIR / 'subdir'.

BASE_DIR = Path(__file__).resolve().parent.parent


ENV_FILE_PATH = BASE_DIR / ".env_base"
load_dotenv(str(ENV_FILE_PATH))

DJANGO_SECRET_KEY= os.environ.get('DJANGO_SECRET_KEY')


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!


#Email setups
EMAIL_HOST          = os.environ.get('EMAIL_HOST')
EMAIL_PORT          =  os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER     = os.environ.get('EMAIL_HOST_USER ')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL  = EMAIL_HOST_USER
EMAIL_BACKEND       = os.environ.get('EMAIL_BACKEND')
EMAIL_USE_TLS       = True
EMAIL_USE_SSL       = False

SECRET_KEY = os.environ.get('DJANGO_SECRET_KEY')

# SECURITY WARNING: don't run with debug turned on in production!

#DEBUG = str(os.environ.get('DEBUG')) == "1"
#ENV_ALLOWED_HOST = os.environ.get("ENV_ALLOWED_HOST")
ALLOWED_HOSTS = ['*']
#if ENV_ALLOWED_HOST:
#     ALLOWED_HOSTS = [ ENV_ALLOWED_HOST ]




# Application definition

INSTALLED_APPS = [
    'usuarios',
    'baton',
    #'account',
    #'courses',
    #'courses_exams',
    #'card_test',
    #'thumbnails',
    #'cart',
   
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
   # 'django.contrib.sites',
    #'django_comments',
    #Wagtail Inicials
    'core',
    #'wagtail',
    'wagtail',
    'wagtailmedia',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    
    
    'wagtail.admin',
   # 'wagtail.core',
   # 'wagtail.contrib.settings',
    'wagtail.contrib.routable_page',
    #'wagtail.contrib.modeladmin',
    #'wagalytics',
    #'wagtailfontawesome',
    'wagtailgmaps',
    'wagtailmenus',
    'django_social_share',
    'taggit',
    
    'webapp_0',
    'streams',
    'widget_tweaks',
   #SMARTQUAIL-BUSINESS-CONSULTING
    #'shop',
    #'coupons',
    #'cart',
    #'todo_en_orden',
    #'coupons',
    #'orders',
    #'contracts',
    #'services',
    #'cart',
    #'cart_c',
    #'payment',
    #'django_phonenumbers',
    #'phonenumber_field',
    'social_django',
    'sorl.thumbnail',
    #'students',
    'embed_video',
    'qr_code',
    'storages',
    #'actions',
    'editorial_literaria',
  
    #'memcache_status',
    'rest_framework',
    'ckeditor',
    'wagtail.contrib.settings',
    
    'baton.autodiscover',
    'memcache_status',
   
]




MIDDLEWARE = [
    #'django.contrib.sites.middleware.CurrentSiteMiddleware',
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.cache.UpdateCacheMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.cache.FetchFromCacheMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'django.contrib.sites.middleware.CurrentSiteMiddleware',
    #'wagtail.core.middleware.SiteMiddleware',
    #'wagtail.contrib.redirects.middleware.RedirectMiddleware',
]

ROOT_URLCONF = 'qnd10app.urls'
WAGTAILADMIN_BASE_URL ='app.smartquail.io'

#WAGTAIL SETUPS
WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.database',
    }
}
#SITE_ID = 1
#WagtailAnalitycs
GA_KEY_CONTENT = os.environ.get('GA_KEY_CONTENT_ENV')
GA_VIEW_ID = os.environ.get('GA_VIEW_ID_ENV')


WAGTAIL_SITE_NAME = 'Smart Business Media'

#RESTFRAMEWORK
REST_FRAMEWORK = {
    'DEFAULT_PERMISSION_CLASSES': [
 'rest_framework.permissions.DjangoModelPermissionsOrAnonReadOnly'
    ]
}

#Redis Setup




REDIS_HOST=os.environ.get('REDIS_HOST')
REDIS_PORT=os.environ.get('REDIS_PORT')
REDIS_DB =os.environ.get('REDIS_DB')  

#DJANGO ADMIN SETUPS

#LOGINGS REDIRECT

#LOGIN_REDIRECT_URL = 'accounts:dashboard'
LOGIN_URL = 'login'
LOGOUT_URL = 'logout'

from django.urls import reverse_lazy
LOGIN_REDIRECT_URL = reverse_lazy('course_list')



#WEBAPP SETTINGS

EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

#Ecommerce App
CART_SESSION_ID = 'cart'

BRAINTREE_MERCHANT_ID = os.environ.get('BRAINTREE_M_ID')
BRAINTREE_PUBLIC_KEY = os.environ.get('BRAINTREE_KEY')
BRAINTREE_PRIVATE_KEY = os.environ.get('BRAINTREE_PRIVATE_KEY')

from braintree import Configuration, Environment
# para desplegar cambiar sandbox con Production
Configuration.configure(
    Environment.Sandbox,
    BRAINTREE_MERCHANT_ID,
    BRAINTREE_PUBLIC_KEY,
    BRAINTREE_PRIVATE_KEY
)

# celery setup
CELERY_BROKER_URL = os.environ.get('CELERY_BROKER_URL')
#CELERY_BROKER_URL = 'amqp://guest:guest@rabbitmq:5672//'
#CELERY_BROKER_URL = 'redis://localhost:6379/0'
CELERY_RESULT_BACKEND = os.environ.get('CELERY_RESULT_BACKEND')
CELERY_ACCEPT_CONTENT = ['application/json']
CELERY_RESULT_SERIALIZER = 'json'
CELERY_TASK_SERIALIZER = 'json'

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
    #'account.authentication.EmailAuthBackend',
    #'social_core.backends.facebook.FacebookOAuth2',
    #'social_core.backends.twitter.TwitterOAuth',
    #'social_core.backends.google.GoogleOAuth2',
]

# social auth settings
SOCIAL_AUTH_FACEBOOK_KEY = os.environ.get('SOCIAL_AUTH_FACEBOOK_KEY')
SOCIAL_AUTH_FACEBOOK_SECRET = os.environ.get('SOCIAL_AUTH_FACEBOOK_SECRET')
SOCIAL_AUTH_FACEBOOK_SCOPE = ['email']

SOCIAL_AUTH_TWITTER_KEY = os.environ.get('SOCIAL_AUTH_TWITTER_KEY')
SOCIAL_AUTH_TWITTER_SECRET =  os.environ.get('SOCIAL_AUTH_TWITTER_SECRET')

SOCIAL_AUTH_GOOGLE_OAUTH2_KEY = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_KEY ')
SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET = os.environ.get('SOCIAL_AUTH_GOOGLE_OAUTH2_SECRET ')



TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [(os.path.join(BASE_DIR, 'templates')),],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'wagtailmenus.context_processors.wagtailmenus',
                'wagtail.contrib.settings.context_processors.settings',
            ],
        },
    },
]

CACHES = {
    'default': {
    'BACKEND': 'django.core.cache.backends.memcached.PyMemcacheCache',
    'LOCATION': '127.0.0.1:11211',
    'TIMEOUT': 60,
    }
}

#CACHES = {
#    'default': {
#        'BACKEND': os.environ.get('CACHE_BACKEND', 'django.core.cache.backends.memcached.MemcachedCache'),
#        'LOCATION': os.environ.get('CACHE_LOCATION', '127.0.0.1:11211'),
#        'TIMEOUT': int(os.environ.get('CACHE_TIMEOUT', 300)),
#    }
#}




WSGI_APPLICATION = 'qnd10app.wsgi.application'

WAGTAILADMIN_BASE_URL =  os.environ.get('DOMAINS')
WAGTAILIMAGES_MAX_UPLOAD_SIZE = 5 * 1024 * 1024 * 1024  # 5 GB en bytes
WAGTAILIMAGES_MAX_IMAGE_PIXELS = 1000000000  # 1 millardo de píxeles (1 Gb)



# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases


#POSTGRES_READY=str(os.environ.get('POSTGRES_READY_ENV'))








# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/








