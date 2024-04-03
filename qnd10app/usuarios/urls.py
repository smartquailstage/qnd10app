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
]
