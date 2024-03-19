from django.urls import path
from . import views
from django.views.decorators.cache import cache_page


app_name = 'announ'

urlpatterns = [
    #URLS CONVOCATORIAS
    path('dashboard/',views.dashboard , name ='dashboard'),
    path('admin_linea_fomento/',views.ManageAnnounListView.as_view(),name='manage_announ_list'),
    path('create_announ/',views.AnnounCreateView.as_view(),name='announ_create'),
    path('<pk>/edit/',views.AnnounUpdateView.as_view(),name='announ_edit'),
    path('<pk>/delete/', views.AnnounDeleteView.as_view(),name='announ_delete'),
]

