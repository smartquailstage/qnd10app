"""
URL configuration for qnd41app project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.urls import path,re_path,include
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from baton.autodiscover import admin
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail import urls as wagtaildocs_urls
from django.contrib.auth import views as auth_views
#from announ.views import AnnounListView
from Fomento_Editorial.views import CourseListView


def UserAdmin(user):
    return  user.is_staff

urlpatterns = [
  
    path('login/', admin.site.urls),  
   # path('analytics/', admin.site.urls),
    path('account/login/', auth_views.LoginView.as_view(), name='login'),
    path('account/logout/', auth_views.LogoutView.as_view(), name='logout'),
   # path('convocatorias_abiertas/',AnnounListView.as_view(), name='announ_list'),
    path('account/', include('account.urls')),
    path('account/password_change/', auth_views.PasswordChangeView.as_view(), name='password_change'),
    path('account/password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),
    # reset password urls
    path('password_reset/', auth_views.PasswordResetView.as_view(), name='password_reset'),
    path('password_reset/done/', auth_views.PasswordResetDoneView.as_view(), name='password_reset_done'),
    path('reset/<uidb64>/<token>/', auth_views.PasswordResetConfirmView.as_view(), name='password_reset_confirm'),
    path('reset/done/', auth_views.PasswordResetCompleteView.as_view(), name='password_reset_complete'),
    path('course/', include('Fomento_Editorial.urls')),
    path('baton/', include('baton.urls')),
    path('courses_list/', CourseListView.as_view(), name='course_list'),
  #  path('students/', include('students.urls')),
   # path('announ/',include('announ.urls')),
    path('social-auth/', include('social_django.urls', namespace='social')),
    path('rosetta/', include('rosetta.urls')),
    re_path(r'^businessmedia/', include(wagtailadmin_urls),name='wagtail'),
    re_path(r'^documents/', include(wagtaildocs_urls)),
    re_path(r'', include(wagtail_urls)),

  ]  + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) 

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)