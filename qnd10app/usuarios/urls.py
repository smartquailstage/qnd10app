from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'usuarios'

urlpatterns = [
    # previous login view
    # path('login/', views.user_login, name='login'),
  
    path('dashboard', views.dashboard, name='dashboard'),
    path('perfil_de_usuario/', views.profile_view , name='perfil'),
    path('configuracion_de_usuario/', views.config_view , name='configuraciones'),
    # change password urls

    # alternative way to include authentication views
    # path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('edit/', views.edit, name='edit'),
    path('edit_contacto_1/', views.edit_contact, name='edit_contact1'),
    path('edit_contacto_2/', views.edit_contact2, name='edit_contact2'),
    path('edit_contacto_3/', views.edit_contact3, name='edit_contact3'),
    path('edit_contacto_4/', views.edit_contact4, name='edit_contact4'),
    path('Actividad_Cultural/', views.edit_activity, name='edit_activity'),
    path('edit_legal1/', views.edit_legal, name='edit_legal'),
    path('edit_legal2/', views.edit_legal2, name='edit_legal2'),
    path('Declaratoria/', views.edit_declaratoria, name='edit_declaratoria'),
    path('confirmacion/', views.confirmacion, name='confirmacion'),

    path('admin/profile/<int:profile_id>/pdf/', views.admin_profile_pdf, name='admin_profile_pdf'),
]
