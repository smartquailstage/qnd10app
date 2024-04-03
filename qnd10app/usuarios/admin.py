from django.contrib import admin
from .models import Profile


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'date_of_birth', 'photo']
    class Meta:
        verbose_name = "Información de perfil de usuario"
        verbose_name_plural = "Información de perfil de usuario"
    