from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


app_name = 'announ'

urlpatterns = [
    path('admin_linea_fomento/',
         views.ManageAnnounListView.as_view(),
         name='manage_announ_list'),
    path('create_announ/',
         views.AnnounCreateView.as_view(),
         name='announ_create'),
    path('<pk>/edit/',
         views.AnnounUpdateView.as_view(),
         name='announ_edit'),
    path('<pk>/delete/',
         views.AnnounDeleteView.as_view(),
         name='announ_delete'),
    path('<pk>/base/',
         views.AnnounBasesUpdateView.as_view(),
         name='announ_base_update'),
    path('base/<int:base_id>/contenido/<model_name>/create/',
         views.AnnounBasesUpdateView.as_view(),
         name='base_contenido_create'),
    path('base/<int:base_id>/contenido/<model_name>/<id>/',
         views.ContenidoCreateUpdateView.as_view(),
         name='base_contenido_update'),
    path('content/<int:id>/delete/',
         views.ContenidoDeleteView.as_view(),
         name='base_contenido_delete'),
    path('base/<int:base_id>/',
         views.BaseContenidoListView.as_view(),
         name='base_contenido_list'),
    path('base/order/',
         views.BaseOrderView.as_view(),
         name='base_order'),
    path('contenido/order/',
         views.ContenidoOrderView.as_view(),
         name='contenido_order'),

     path('enroll-announ/',
         views.PostulantesEnrollAnnounView.as_view(),
         name='postulante_enroll_announ'),

     path('convocatorias/',
         views.PostulantesAnnounListView.as_view(),
         name='postulante_announ_list'),

      path('categoria/<slug:categoria>)/',
         views.AnnounListView.as_view(),
         name='announ_list_categoria'),

    path('<slug:slug>/',
         views.AnnounDetailView.as_view(),
         name='announ_detail'),

     path('announ/<pk>/',
         cache_page(60 * 15)(views.PostulantesAnnounDetailView.as_view()),
         name='postulante_announ_detail'),

     path('announ/<pk>/<base_id>/',
         cache_page(60 * 15)(views.PostulantesAnnounDetailView.as_view()),
         name='postulante_announ_detail_base'),
]