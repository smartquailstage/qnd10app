from django.urls import path,re_path,include
from django.conf.urls.static import static
from django.urls import path
from django.conf import settings
from django.conf.urls.i18n import i18n_patterns
from baton.autodiscover import admin
from wagtail.admin import urls as wagtailadmin_urls
from wagtail import urls as wagtail_urls
from wagtail import urls as wagtaildocs_urls

urlpatterns = [
    path('admin/', admin.site.urls),
]
