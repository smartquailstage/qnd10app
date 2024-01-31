from .base import *

ENV_FILE_PATH = BASE_DIR / ".env_dev"
load_dotenv(str(ENV_FILE_PATH))




# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = os.environ.get("DEBUG")
ALLOWED_HOSTS = [os.environ.get("ENV_ALLOWED_HOST")]

WAGTAILADMIN_BASE_URL = os.environ.get("WAGTAILADMIN_BASE_URL")  
#Nombre del sitio web
WAGTAIL_SITE_NAME =os.environ.get("WAGTAIL_SITE_NAME")  

WAGTAILIMAGES_MAX_UPLOAD_SIZE = 30 * 1024 * 1024   # 15mb
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'

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

ROOT_URLCONF = os.environ.get("ROOT_URLCONF")
WSGI_APPLICATION = os.environ.get("WSGI_APPLICATION")

LOCALE_PATHS = (
    os.path.join(BASE_DIR, 'locale/'),
)

WAGTAILADMIN_BASE_URL =  os.environ.get('DOMAINS')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR / 'db.sqlite3'),
    }
}

SITE_ID = 1
WAGTAILADMIN_BASE_URL = "/businessmedia/"

REDIS_HOST=os.environ.get('REDIS_HOST')
REDIS_PORT=os.environ.get('REDIS_PORT')
REDIS_DB =os.environ.get('REDIS_DB')  



BATON = {
    'SITE_HEADER': '<img src="/static/img/logo_flor.png" width="180px" >',
    'SITE_TITLE': 'Isla Floreana CC',
    'INDEX_TITLE': 'Administración- Centro comunitario Isla Floreana',
    #'SUPPORT_HREF': 'https://github.com/otto-torino/django-baton/issues',
    'COPYRIGHT': 'copyright © 2022 <a href="#">Isla Floreana Centro Comunitario</a>', # noqa
    'POWERED_BY': '<img src="/static/img/logo.png" width="40px" >',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'CHANGELIST_FILTERS_IN_MODAL': True,
    'CHANGELIST_FILTERS_ALWAYS_OPEN': False,
    'CHANGELIST_FILTERS_FORM': True,
    'MENU_ALWAYS_COLLAPSED': False,
    'MENU_TITLE': 'Isla Floreana',
    'MESSAGES_TOASTS': True,
    'GRAVATAR_DEFAULT_IMG': 'retro',
    'LOGIN_SPLASH': '/static/img/3.jpg',
    'LOGOUT_SPLASH': '/static/img/3.jpg',
    'SEARCH_FIELD': {
        'label': 'Search contents...',
        'url': '/search/',
    },
    'MENU': (
        { 'type': 'title', 'label': 'Smart Office', 'apps': ('auth', ) },
        {
            'type': 'app',
            'name': 'auth',
            'label': 'Authentication',
            'icon': 'fa fa-lock',
            'models': (
                {
                    'name': 'user',
                    'label': 'Users'
                },
                {
                    'name': 'group',
                    'label': 'Groups'
                },
            )
        },

        {
            'type': 'app',
            'name': 'orders',
            'label': 'Reservas',
            'icon': 'fa fa-folder-open',
            'models': (
                {
                    'name': 'order',
                    'label': 'Reservas Online'
                },
                {
                    'name': 'group',
                    'label': 'Groups'
                },
            )
        },

        { 'type': 'title', 'label': 'Contents', 'apps': ('flatpages', ) },
        { 'type': 'model', 'label': 'Pages', 'name': 'flatpage', 'app': 'flatpages' },
        { 'type': 'free', 'label': 'Custom Link', 'url': 'http://www.google.it', 'perms': ('flatpages.add_flatpage', 'auth.change_user') },
        { 'type': 'free', 'label': 'My parent voice', 'default_open': True, 'children': [
            { 'type': 'model', 'label': 'A Model', 'name': 'mymodelname', 'app': 'myapp' },
            { 'type': 'free', 'label': 'Another custom link', 'url': 'http://www.google.it' },
        ] },
    ),
}



ADMINS= (
    ('SILVA MAU', 'smartquail.dev@gmail.com')
)

ALLOWED_HOSTS = ['*']

#Static files DevMod

MEDIA_URL = "/media/"
MEDIA_ROOT  = os.path.join(BASE_DIR, 'media')
STATICFILES_DIRS = [BASE_DIR / "staticfiles"]  
STATIC_URL = "/static/"
STATIC_ROOT = STATIC_ROOT = BASE_DIR / "static"

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'


# celery setup

#CELERY_BROKER_URL = 'amqp://guest:guest@rabbitmq:5672//'
CELERY_BROKER_URL = 'redis://localhost:6379/0'


EMAIL_HOST= "smtp.gmail.com"
EMAIL_PORT=  "443"
#EMAIL_USE_TLS=  "True"
EMAIL_HOST_USER= "smartquail.info@gmail.com"
EMAIL_HOST_PASSWORD= "pzmblsxbqyvdzuxz"
DEFAULT_FROM_EMAIL= "EMAIL_HOST_USER"
EMAIL_BACKEND= "django.core.mail.backends.smtp.EmailBackend"
#EMAIL_USE_TLS       = "True"
#EMAIL_USE_SSL= "False"

CELERY_BROKER_URL="redis://127.0.0.1:6379/0"
CELERY_RESULT_BACKEND="redis://127.0.0.1:6379/0"

REDIS_HOST=os.environ.get('REDIS_HOST')
REDIS_PORT=os.environ.get('REDIS_PORT')
REDIS_DB =os.environ.get('REDIS_DB')  