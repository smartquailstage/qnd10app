from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    # previous login view
    # path('login/', views.user_login, name='login'),
  
    path('dashboard', views.dashboard, name='dashboard'),
    # change password urls

    # alternative way to include authentication views
    # path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('inscripcion/', views.detalle_manual , name='detalle_manual'),
    path('postulacion/', views.detalle_manual_lineafomento , name='detalle_manual_lineafomento'),
    path('crear_convocatoria/', views.detalle_manual_creacion_convocatoria_fomento , name='detalle_manual_creacion_convocatoria_fomento'),
    path('editar_convocatoria/', views.detalle_manual_editar_convocatoria_fomento , name='detalle_manual_editar_convocatoria_fomento'),
    path('configuraciones/', views.detalle_manual_editar_configuracion , name='detalle_manual_editar_configuracion'),
    path('edit/', views.edit, name='edit'),
    path('edit_contact/', views.edit_contact, name='edit_contact'),
    path('edit_legal/', views.edit_legal, name='edit_legal'),
    path('edit_representante_legal/', views.edit2_legal,name='edit_legal2'),
    path('edit_activity/', views.edit_activity, name='edit_activity'),
    path('edit_done/', views.edit_done, name='edit_done'),
    path('terms/', views.edit_terms, name='edit_terms'),
    path('profile/', views.perfil_usuario, name='user_profile'),
   # path('postulantes_profile/', views.edit_postulantes, name='user_postulantes_profile'),
    path('admin/profile/<int:perfil_id>/pdf/', views.admin_profile_pdf, name='admin_profile_pdf'),
    path('admin/contacto/<int:contacto_id>/pdf/', views.admin_contact_pdf, name='admin_contact_pdf'),
    path('admin/legal/<int:info_legal_id>/pdf/', views.admin_legal_pdf, name='admin_legal_pdf'),
    path('admin/contacto_lega/<int:contactolegal_id>/pdf/', views.admin_contact_legal_pdf, name='admin_contact_legal_pdf'),
    path('admin/actividad_cultural/<int:actividad_id>/pdf/', views.admin_activity_pdf, name='admin_activity_pdf'),
    path('admin/declaratoria/<int:terms_id>/pdf/', views.admin_terms_pdf, name='admin_terms_pdf'),
]
