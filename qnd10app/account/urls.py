from django.urls import path, include
from django.contrib.auth import views as auth_views
from . import views

app_name = 'account'

urlpatterns = [
    # previous login view
    # path('login/', views.user_login, name='login'),
    path('login/', auth_views.LoginView.as_view(), name='login'),
    path('logout/', auth_views.LogoutView.as_view(), name='logout'),
    path('dashboard', views.dashboard, name='dashboard'),
    # change password urls

    # alternative way to include authentication views
    # path('', include('django.contrib.auth.urls')),
    path('register/', views.register, name='register'),
    path('inscripcion/', views.detalle_manual , name='detalle_manual'),
    path('edit/', views.edit, name='edit'),
    path('edit_contact/', views.edit_contact, name='edit_contact'),
    path('edit_legal/', views.edit_legal, name='edit_legal'),
    path('edit_representante_legal/', views.edit2_legal,name='edit_legal2'),
    path('edit_activity/', views.edit_activity, name='edit_activity'),
    path('edit_done/', views.edit_done, name='edit_done'),
    path('terms/', views.edit_terms, name='edit_terms'),
    path('profile/', views.perfil_usuario, name='user_profile'),
]
