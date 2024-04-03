from django.db import models
from django.conf import settings


class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Nombre de Usuario")
    date_of_birth = models.DateField(blank=True, null=True,verbose_name="Fecha de Nacimiento")
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, verbose_name="Foto de Perfil")

    def __str__(self):
        return 'Perfil de Usuario {}'.format(self.user.username)