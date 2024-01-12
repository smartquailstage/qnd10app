from .base import *

ENV_FILE_PATH = BASE_DIR / ".env_stage"
load_dotenv(str(ENV_FILE_PATH))

DEBUG =  os.environ.get("DEBUG") 


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/4.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = os.environ.get("DJANGO_SECRET_KEY")

# SECURITY WARNING: don't run with debug turned on in production!
#DEBUG = os.environ.get("DEBUG")
ALLOWED_HOSTS = [os.environ.get("ENV_ALLOWED_HOST")]


#Nombre del sitio web
WAGTAIL_SITE_NAME =os.environ.get("WAGTAIL_SITE_NAME")  
WAGTAILADMIN_BASE_URL = os.environ.get("WAGTAILADMIN_BASE_URL") 

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



BATON = {
    'SITE_HEADER': '<a href="#"><img src="/static/img/m2.png" height="26px"></a>',
    'SITE_TITLE': '',
    'INDEX_TITLE': 'BUSINESS ANALITYCS PLATFORM ',
    'SUPPORT_HREF': '#',
    'COPYRIGHT': '<a href="#"><img src="/static/img/m2.png" height="18px"></a>&nbsp;&nbsp; copyright © 2022', # noqa
    'POWERED_BY': '<a href="#"><img src="/static/img/logo_smartquailgray.png" height="13px"</a>',
    'CONFIRM_UNSAVED_CHANGES': True,
    'SHOW_MULTIPART_UPLOADING': True,
    'ENABLE_IMAGES_PREVIEW': True,
    'CHANGELIST_FILTERS_IN_MODAL': True,
    'CHANGELIST_FILTERS_ALWAYS_OPEN': False,
    'CHANGELIST_FILTERS_FORM': True,
    'MENU_ALWAYS_COLLAPSED': True,
    'MENU_TITLE': 'Todo en Orden',
    'MESSAGES_TOASTS': False,
    'GRAVATAR_DEFAULT_IMG': 'retro',
    'LOGIN_SPLASH': '/static/img/login_splash.jpg',
    'SEARCH_FIELD': {
        'label': 'Search contents...',
         'url': '/search/',
    },
    'MENU': (
        { 'type': 'title', 'label': 'Gerencia', 'apps': ('auth','todo_en_orden', ) },
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
            'name': 'todo_en_orden',
            'label': 'Dpto Contable',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
        {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Dpto Operativo',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
         {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Dpto RRHH',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
        {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Dpto Legal',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
        {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Dpto Marketing',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
         { 'type': 'title', 'label': 'Administración Operativa', 'apps': ('auth','todo_en_orden', ) },
              {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Entradas y salidas',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
         {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Propuestas',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
         {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Servicios',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
        {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Insumos Venta',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
         {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Insumos Contratos ',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
                 {
            'type': 'app',
            'name': 'todo_en_orden',
            'label': 'Generador de Contratos ',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'order',
                    'label': 'Clientes'
                },
                {
                    'name': 'order',
                    'label': 'Servicios'
                },
            )
        },
        
         
    ),
}




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR / 'db.sqlite3')
    }
}

DB_USERNAME = os.environ.get("POSTGRES_USER")
DB_PASSWORD = os.environ.get("POSTGRES_PASSWORD")
DB_DATABASE = os.environ.get("POSTGRES_DB")
DB_HOST = os.environ.get("POSTGRES_HOST")
DB_PORT = os.environ.get("POSTGRES_PORT")
DB_IS_AVIAL = all([
    DB_USERNAME,
    DB_PASSWORD,
    DB_DATABASE,
    DB_HOST,
    DB_PORT
])

POSTGRES_READY="1"
if DB_IS_AVIAL and POSTGRES_READY:
    DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': DB_DATABASE,
        "USER": DB_USERNAME,
        "PASSWORD": DB_PASSWORD,
        "HOST": DB_HOST,
        "PORT": DB_PORT,
    }
}
    
SITE_ID = 1


REDIS_HOST=os.environ.get('REDIS_HOST')
REDIS_PORT=os.environ.get('REDIS_PORT')
REDIS_DB =os.environ.get('REDIS_DB')  


#Email setups
EMAIL_HOST          = os.environ.get('EMAIL_HOST')
EMAIL_PORT          =  os.environ.get('EMAIL_PORT')
EMAIL_HOST_USER     = os.environ.get('EMAIL_HOST_USER ')
EMAIL_HOST_PASSWORD = os.environ.get('EMAIL_HOST_PASSWORD')
DEFAULT_FROM_EMAIL  = EMAIL_HOST_USER
EMAIL_BACKEND       = os.environ.get('EMAIL_BACKEND')
EMAIL_USE_TLS       = True
EMAIL_USE_SSL       = False


DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

STATIC_URL = '/static/'
STATIC_ROOT = BASE_DIR / "static"

STATICFILES_DIRS = [
    BASE_DIR / "staticfiles"
]

MEDIA_URL = "/media/"
MEDIA_ROOT = BASE_DIR / "media"
MEDIAFILES_DIRS = [
    BASE_DIR / "mediafiles"
]

from .cdn.conf import * # noqa

