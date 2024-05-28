from django.urls import path
from . import views

app_name = 'actividades_espacio_publico'

urlpatterns = [
    #path('proponer_actividad/', views.crear_evento, name='event_create'),
    path('proponer_actividades_espacio_publico/evento/<slug:categoria_slug>/', views.evento, name='evento'),
    path('eventos/', views.listar_categorias, name='listar_categorias'),
]