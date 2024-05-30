from django.urls import path
from . import views

app_name = 'actividades_espacio_publico'

urlpatterns = [
    #path('proponer_actividad/', views.crear_evento, name='event_create'),
   # path('proponer_actividades_espacio_publico/evento/<slug:categoria_slug>/', views.evento, name='evento'),
    path('eventos_30000/', views.evento_30000, name='evento_30000'),
    path('crear_propuesta_evento/', views.crear_propuesta_evento_30000, name='crear_propuesta_evento'),
    path('eventos_20000/', views.evento_20000, name='evento_20000'),
    path('crear_propuesta_evento_20000/', views.crear_propuesta_evento_20000, name='crear_propuesta_evento_20000'),
    path('eventos_10000/', views.evento_10000, name='evento_10000'),
    path('crear_propuesta_evento_10000/', views.crear_propuesta_evento_10000, name='crear_propuesta_evento_10000'),
    path('eventos_5000/', views.evento_5000, name='evento_5000'),
    path('crear_propuesta_evento_5000/', views.crear_propuesta_evento_5000, name='crear_propuesta_evento_5000'),
    path('eventos/', views.listar_categorias, name='listar_categorias'),
    path('admin/evento/<int:profile_id>/pdf/', views.admin_evento_30000_pdf, name='admin_evento_30000_pdf'),
    path('admin/evento/<int:profile_id>/pdf_20000/', views.admin_evento_20000_pdf, name='admin_evento_20000_pdf'),
    path('admin/evento/<int:profile_id>/pdf_10000/', views.admin_evento_10000_pdf, name='admin_evento_10000_pdf'),
    path('admin/evento/<int:profile_id>/pdf_5000/', views.admin_evento_5000_pdf, name='admin_evento_5000_pdf'),
    path('success/', views.evento_success, name='evento_success'),
    path('fail/', views.evento_fail, name='evento_fail'),
]