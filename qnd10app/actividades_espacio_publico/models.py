from django.db import models
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from django.contrib.auth.models import User
from django.urls import reverse
from django.conf import settings



class Subject(models.Model):

    CATEGORIAS = (
        (30000, 'Evento 30000'),
        (20000, 'Evento 20000'),
        (10000, 'Evento 10000'),
        (5000, 'Circulación 5000'),
    )
    
    COLORS = (
    ('primary', 'Verde'),
    ('warning', 'Amarillo'),
    ('danger', 'Rojo'),
    ('dark', 'Negro'),
    )
    categoria = models.IntegerField(choices=CATEGORIAS)
    slug = models.SlugField(max_length=200, unique=True)
    description = models.CharField(max_length=200,verbose_name="Descripción")
    colores = models.CharField(choices=COLORS,max_length=200,null=True,blank=True)
    url = models.CharField(max_length=200,verbose_name="Evento_url",null= True, blank= True)


    class Meta:
        ordering = ['categoria']
        verbose_name_plural = "Categorias de Eventos" 


    def get_absolute_url(self):
        # Generar la URL de la vista 'evento' con el slug de la categoría actual
        return reverse('actividades_espacio_publico:evento', kwargs={'categoria_slug': self.slug})

    def __str__(self):
        return self.slug

class Evento(models.Model):
    usuario = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Nombre de Usuario")
    evento= models.ForeignKey(Subject,
                                related_name='eventos',
                                on_delete=models.CASCADE, null= True, blank= True)
    servicios_artisticos = models.DecimalField(max_digits=10, decimal_places=2,null= True, blank= True)
    rider_tecnico = models.IntegerField(choices=[(15000, '15000'), (10000, '10000'), (4000, '4000')],null= True, blank= True)
    direccion_artistica = models.DecimalField(max_digits=10, decimal_places=2,null= True, blank= True)
    aforo = models.IntegerField(null= True, blank= True)
    ediciones_anteriores = models.BooleanField(default=False, help_text="Marque si el evento al que usted desea proponer tiene ediciones anteriores.",null= True, blank= True)
    actividades_academicas_complementarias = models.TextField(null= True, blank= True)
    actividades_emprendimiento_complementarias = models.TextField(null= True, blank= True)

   

 


class Evento_30000(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Nombre de Usuario")
    evento= models.ForeignKey(Subject,
                                related_name='eventos_30000',
                                on_delete=models.CASCADE, null= True, blank= True)
    servicios_artisticos = models.DecimalField(max_digits=10, decimal_places=2,null= True, blank= True)
    rider_tecnico = models.IntegerField(choices=[(15000, '15000'), (10000, '10000'), (4000, '4000')],null= True, blank= True)
    direccion_artistica = models.DecimalField(max_digits=10, decimal_places=2,null= True, blank= True)
    aforo = models.IntegerField(null= True, blank= True)
    ediciones_anteriores = models.BooleanField(default=False, help_text="Marque si el evento al que usted desea proponer tiene ediciones anteriores.",null= True, blank= True)
    actividades_academicas_complementarias = models.TextField(null= True, blank= True)
    actividades_emprendimiento_complementarias = models.TextField(null= True, blank= True)

    def __str__(self):
        return self.user.first_name



    

class Evento_20000(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Nombre de Usuario")
    evento= models.ForeignKey(Subject,
                                related_name='eventos_20000',
                                on_delete=models.CASCADE, null= True, blank= True)
    servicios_artisticos = models.DecimalField(max_digits=10, decimal_places=2,null= True, blank= True)
    rider_tecnico = models.IntegerField(choices=[(15000, '15000'), (10000, '10000'), (4000, '4000')],null= True, blank= True)
    direccion_artistica = models.DecimalField(max_digits=10, decimal_places=2,null= True, blank= True)
    aforo = models.IntegerField(null= True, blank= True)
    ediciones_anteriores = models.BooleanField(default=False, help_text="Marque si el evento al que usted desea proponer tiene ediciones anteriores.",null= True, blank= True)
    actividades_academicas_complementarias = models.TextField(null= True, blank= True)
    actividades_emprendimiento_complementarias = models.TextField(null= True, blank= True)

    
class Evento_10000(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Nombre de Usuario")
    evento= models.ForeignKey(Subject,
                                related_name='eventos_10000',
                                on_delete=models.CASCADE, null= True, blank= True)
    servicios_artisticos = models.DecimalField(max_digits=10, decimal_places=2,null= True, blank= True)
    rider_tecnico = models.IntegerField(choices=[(15000, '15000'), (10000, '10000'), (4000, '4000')],null= True, blank= True)
    direccion_artistica = models.DecimalField(max_digits=10, decimal_places=2,null= True, blank= True)
    aforo = models.IntegerField(null= True, blank= True)
    ediciones_anteriores = models.BooleanField(default=False, help_text="Marque si el evento al que usted desea proponer tiene ediciones anteriores.",null= True, blank= True)
    actividades_academicas_complementarias = models.TextField(null= True, blank= True)
    actividades_emprendimiento_complementarias = models.TextField(null= True, blank= True)



class Evento_5000(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Nombre de Usuario")
    evento= models.ForeignKey(Subject,
                                related_name='eventos_5000',
                                on_delete=models.CASCADE, null= True, blank= True)
    servicios_artisticos = models.DecimalField(max_digits=10, decimal_places=2,null= True, blank= True)
    rider_tecnico = models.IntegerField(choices=[(15000, '15000'), (10000, '10000'), (4000, '4000')],null= True, blank= True)
    direccion_artistica = models.DecimalField(max_digits=10, decimal_places=2,null= True, blank= True)
    aforo = models.IntegerField(null= True, blank= True)
    ediciones_anteriores = models.BooleanField(default=False, help_text="Marque si el evento al que usted desea proponer tiene ediciones anteriores.",null= True, blank= True)
    actividades_academicas_complementarias = models.TextField(null= True, blank= True)
    actividades_emprendimiento_complementarias = models.TextField(null= True, blank= True)

 
    
