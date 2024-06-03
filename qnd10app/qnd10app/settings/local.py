from .base import *

DEBUG=  "1"




DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(BASE_DIR / 'db.sqlite3'),
    }
}



BATON = {
    'SITE_HEADER': '<a href="#"><img src="/static/img/m2.png" height="26px"></a>',
    'SITE_TITLE': '',
    'INDEX_TITLE': 'Secretaría de Cultura- Distrito Metropolitano de Quito. ',
    'SUPPORT_HREF': '#',
    'COPYRIGHT': '<a href="#"><img src="/static/img/m2.png" height="18px"></a>&nbsp;&nbsp; copyright © 2024', # noqa
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
   
    'MENU': (
       
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
         { 'type': 'title', 'label': 'Dirección Espacio Público', 'apps': ('auth','todo_en_orden', ) },
         {
            'type': 'app',
            'name': 'actividades_espacio_publico',
            'label': 'Propuestas',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'subject',
                    'label': 'Administración de eventos'
                },
                {
                    'name': 'evento_30000',
                    'label': 'Evento 30000'
                },
                 {
                    'name': 'evento_20000',
                    'label': 'Evento 20000'
                },
                {
                    'name': 'evento_10000',
                    'label': 'Evento 10000'
                },
                {
                    'name': 'evento_5000',
                    'label': 'Evento 5000'
                },
              
            )
        },
         { 'type': 'title', 'label': 'Dirección Creatividad & Fomento', 'apps': ('auth','todo_en_orden', ) },
        {
            'type': 'app',
            'name': 'editorial_literaria',
            'label': 'Editorial & literario',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'subject',
                    'label': 'Categorías de convocatorias'
                },
                {
                    'name': 'course',
                    'label': 'Convocatorias realizadas'
                },
                
                {
                    'name': 'module',
                    'label': 'Bases técnicas inscriptas en convocatorias'
                },
              
            )
        },
         {
            'type': 'app',
            'name': 'proyectos',
            'label': 'Proyectos postulados',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'subject',
                    'label': 'Volumenes editoriales'
                },
                {
                    'name': 'project',
                    'label': 'Proyectos editoriales '
                },
            )
        },

         { 'type': 'title', 'label': 'Administración de perfiles', 'apps': ('auth','todo_en_orden', ) },
              {
            'type': 'app',
            'name': 'usuarios',
            'label': 'Administración de usuarios',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'profile',
                    'label': 'Perfil de usuarios'
                },
                {
                    'name': 'contacts',
                    'label': 'Perfil de contactos'
                },
                {
                    'name': 'legal',
                    'label': 'Perfil de personería'
                },
                {
                    'name': 'activity',
                    'label': 'Perfil de actividad cultural'
                },
                {
                    'name': 'declaracionveracidad',
                    'label': 'declaratorias'
                },
            )
        },
         { 'type': 'title', 'label': 'Comunicación', 'apps': ('auth','todo_en_orden', ) },
         {
            'type': 'app',
            'name': 'usuarios',
            'label': 'Información y Normativas',
            'icon': 'fa fa-user',
            'models': (
                {
                    'name': 'dashboard',
                    'label': 'Pagina de Inicio'
                },
                {
                    'name': 'privacypolicy',
                    'label': 'Políticas de privacidad Fomento editorial'
                },
                {
                    'name': 'termsofuse',
                    'label': 'Condiciones de uso Fomento editorial'
                },

                {
                    'name': 'activityprivacypolicy',
                    'label': 'Políticas de privacidad Espacio público'
                },
                 {
                    'name': 'activitytermsofuse',
                    'label': 'Condiciones de uso Espacio público'
                },


            )
        },
   

        
         
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

