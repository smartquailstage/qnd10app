"""
Django settings for testnodos project.

Generated by 'django-admin startproject' using Django 4.2.6.

For more information on this file, see
https://docs.djangoproject.com/en/4.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/4.2/ref/settings/
"""
import os
from pathlib import Path
from dotenv import load_dotenv
from decouple import config

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent



# Application definition

INSTALLED_APPS = [
    'baton',
    'wagtail',
    'django.contrib.sites',
    #'courses',
    #'courses_exams',
    #'card_test',
    #'thumbnails',
    #'cart',
    "wagtail_localize",
    'django.contrib.contenttypes',
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.humanize',
    #'storages',
    #Wagtail Inicials
    'core',
    #'wagtail.locales',
    "wagtail_modeladmin",
    'wagtail_localize.locales',
    'wagtail.contrib.forms',
    'wagtail.contrib.redirects',
    'wagtail.embeds',
    'wagtail.sites',
    'wagtail.users',
    'wagtail.snippets',
    'wagtail.documents',
    'wagtail.images',
    'wagtail.search',
    'wagtail.hooks',
    #'wagtail.locales',
    #"wagtail_localize",
   # 'wagtail.core',
    
 
     
    #'wagtail.locales',
    #'wagtail.contrib.simple_translation',
    'wagtail.admin',
    'wagtail.contrib.settings',
    'wagtail.contrib.routable_page',
   # 'wagtail.contrib.modeladmin',
    #'wagalytics',
    #'wagtailfontawesome',
    'wagtailgmaps',
    'wagtailmenus',
    #'django_social_share',
    'taggit',
    'django_social_share',
    'streams',
    'widget_tweaks',
   # 'wagtailcaptcha',
   #SMARTQUAIL-BUSINESS-CONSULTING
  
    'social_django',
    'sorl.thumbnail',
    #'students',
    'embed_video',
    'qr_code',
#    'actions',
  
    
    'baton.autodiscover',   
    #'memcache_status',
    'rest_framework',
    'ckeditor',
    'rosetta',
    
    
]

MIDDLEWARE = [
    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.middleware.csrf.CsrfViewMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    'wagtail.contrib.redirects.middleware.RedirectMiddleware',
    'django.middleware.locale.LocaleMiddleware',
]




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
                'django.template.context_processors.i18n',
            ],
        },
    },
]


SITE_ID = 1



# Database
# https://docs.djangoproject.com/en/4.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}


# Password validation
# https://docs.djangoproject.com/en/4.2/ref/settings/#auth-password-validators

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

AUTHENTICATION_BACKENDS = [
    'django.contrib.auth.backends.ModelBackend',
   # 'account.authentication.EmailAuthBackend',
    'social_core.backends.facebook.FacebookOAuth2',
    'social_core.backends.twitter.TwitterOAuth',
    'social_core.backends.google.GoogleOAuth2',
]

CART_SESSION_ID = 'cart'
SBLCART_SESSION_ID = 'cart'
SBACART_SESSION_ID = 'cart'
SBTCART_SESSION_ID = 'cart'
SBMCART_SESSION_ID = 'cart'

USE_I18N = True
WAGTAIL_I18N_ENABLED = True
USE_L10N = True


# Internationalization
# https://docs.djangoproject.com/en/4.2/topics/i18n/



from django.utils.translation import gettext_lazy as _

#WAGTAIL SETTINGS:

WAGTAIL_CONTENT_LANGUAGES = LANGUAGES = [
    ('en', _("English")),
    ('fr', _("French")),
    ('es', _("Spanish")),
]

WAGTAILFORMS_NOTIFICATION_FROM_EMAIL = 'info@smartquail.io'
WAGTAILFORMS_NOTIFICATION_TEMPLATE = 'forms/notification_email.txt'

WAGTAIL_I18N_ENABLED = True

WAGTAILSEARCH_BACKENDS = {
    'default': {
        'BACKEND': 'wagtail.search.backends.database',
    }
}



USE_L10N = True

LANGUAGE_CODE = 'es'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True



# Default primary key field type
# https://docs.djangoproject.com/en/4.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

