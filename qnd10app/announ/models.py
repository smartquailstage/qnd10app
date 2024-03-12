from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from django.db.models.signals import post_save
from django.dispatch import receiver
from datetime import timedelta
from django.utils import timezone


class Categoria_linea_fomento_editorial(models.Model):
    title = models.CharField(max_length=200, verbose_name="Nombre de categoria")
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']

    def __str__(self):
        return self.title


class announ_linea_fomento_editorial(models.Model):
    owner = models.ForeignKey(User,
                              related_name='announ_created',
                              on_delete=models.CASCADE)
    portada = models.FileField(upload_to='documentos/portadas/', null=True, blank=True)
    categoria = models.ForeignKey(Categoria_linea_fomento_editorial,
                                  related_name='announces',
                                  on_delete=models.CASCADE,
                                  verbose_name="Nombre de Categoría de la convocatoria")
    title = models.CharField(max_length=200, verbose_name="Nombre de convocatoria")
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField(verbose_name="Descripción de Convocatoria")
    created = models.DateTimeField(auto_now_add=True)
    fecha_inicio = models.DateTimeField(null=True, blank=True)
    fecha_vencimiento = models.DateTimeField(null=True, blank=True)
    dias_diferencia = models.IntegerField(default=0,null=True, blank=True)
    horas_diferencia = models.IntegerField(default=0,null=True, blank=True)
    minutos_diferencia = models.IntegerField(default=0,null=True, blank=True)
    segundos_diferencia = models.IntegerField(default=0,null=True, blank=True)
    dias_diferencia_activacion = models.IntegerField(default=0,null=True, blank=True)
    horas_diferencia_activacion = models.IntegerField(default=0,null=True, blank=True)
    minutos_diferencia_activacion = models.IntegerField(default=0,null=True, blank=True)
    segundos_diferencia_activacion = models.IntegerField(default=0,null=True, blank=True)
    actividad = models.BooleanField(null=True, blank=True, verbose_name="Estado de la actividad de la convocatoría")

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title

    def calcular_diferencia(self):
        # Verifica si ambas fechas tienen valor
        if self.fecha_inicio and self.fecha_vencimiento:
            # Calcula la diferencia entre las dos fechas
            diferencia = self.fecha_vencimiento - self.fecha_inicio
            diferencia_activacion = self.fecha_inicio - self.created

            # Extrae los componentes de la diferencia
            dias = diferencia.days
            segundos_totales = diferencia.total_seconds()
            dias_activacion = diferencia_activacion.days
            segundos_totales_activacion = diferencia_activacion.total_seconds()

            # Calcula las horas y segundos restantes
            horas = int(segundos_totales // 3600)
            segundos_restantes = int(segundos_totales % 3600)
            horas_activacion = int(segundos_totales_activacion // 3600)
            segundos_restantes_activacion = int(segundos_totales_activacion % 3600)

            # Calcula los minutos y segundos restantes
            minutos = int(segundos_restantes // 60)
            segundos = int(segundos_restantes % 60)
            minutos_activacion = int(segundos_restantes_activacion // 60)
            segundos_activacion = int(segundos_restantes_activacion % 60)

            # Grabar los valores calculados
            self.dias_diferencia = dias
            self.horas_diferencia = horas
            self.minutos_diferencia = minutos
            self.segundos_diferencia = segundos
            self.dias_diferencia_activacion = dias_activacion
            self.horas_diferencia_activacion = horas_activacion
            self.minutos_diferencia_activacion = minutos_activacion
            self.segundos_diferencia_activacion = segundos_activacion

            # Si todos los componentes de la diferencia de activación son cero, establecer la actividad en False
            if dias_activacion == horas_activacion == minutos_activacion == segundos_activacion == 0:
                self.actividad = True
            else:
                self.actividad = False

          

            return {
                'dias': dias,
                'horas': horas,
                'minutos': minutos,
                'segundos': segundos
            }
        else:
            return None

@receiver(post_save, sender=announ_linea_fomento_editorial)
def grabar_diferencia(sender, instance, created, **kwargs):
    instance.calcular_diferencia()




class bases_linea_fomento_editorial(models.Model):
    base = models.ForeignKey(announ_linea_fomento_editorial,
                               related_name='bases',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['base'])

    class Meta:
            ordering = ['order']

    def __str__(self):
        return '{}. {}'.format(self.order, self.title)


class contenido_bases_linea_fomento_editorial(models.Model):
    base = models.ForeignKey(bases_linea_fomento_editorial,
                               related_name='contenidos_bases',
                               on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                     limit_choices_to={'model__in':('text',
                                                                    'video',
                                                                    'image',
                                                                    'file')},
                                     on_delete=models.CASCADE,verbose_name="Tipo de Contenido de las bases")
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['base'])

    class Meta:
            ordering = ['order']


class ItemBase(models.Model):
    owner = models.ForeignKey(User,
                              related_name='%(class)s_related',
                              on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title


class Text(ItemBase):
    content = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='files')

class Image(ItemBase):
       file = models.FileField(upload_to='images')

class Video(ItemBase):
    url = models.URLField()
