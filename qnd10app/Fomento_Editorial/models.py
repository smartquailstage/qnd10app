from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe

class Fomento(models.Model):
    title = models.CharField(max_length=200, verbose_name="Escriba el nombre de la línea de fomento correspondiente")
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Categorías de Fomento"
        verbose_name_plural = "Categoría de Fomento"
        ordering = ['title']

    def __str__(self):
        return self.title
class Subject(models.Model):
    title = models.CharField(max_length=200, verbose_name="Escriba el nombre de la categoría de convocatoria correspondiente")
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        verbose_name = "Categorías de Convocatorias"
        verbose_name_plural = "Categoría de Convocatoria"
        ordering = ['title']


    def __str__(self):
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(User,
                              related_name='courses_created',
                              on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,
                                related_name='courses',
                                on_delete=models.CASCADE,verbose_name="Categoría de convocatoria", null=True, blank=True)
    fomento = models.ForeignKey(Fomento,
                                related_name='fomento',
                                on_delete=models.CASCADE,verbose_name="Línea de fomento", null=True, blank=True)
    title = models.CharField(max_length=200, verbose_name="Nombre de Convocatoria")
    portada = models.FileField(upload_to='documentos/portadas/', null=True, blank=True)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateField(auto_now_add=True)
    fecha_inicio = models.DateField(null=True, blank=True)
    fecha_vencimiento = models.DateField(null=True, blank=True)
    actividad = models.BooleanField(null=True, blank=True, verbose_name="¿Desea activar esta convocatoria ?")
    students = models.ManyToManyField(User,
                                      related_name='courses_joined',
                                      blank=True,verbose_name="Usuarios Postulantes")
    
    def calcular_diferencia_dias(self):
        if self.created and self.fecha_vencimiento:
            diferencia = self.fecha_vencimiento - self.created
            return diferencia.days
        else:
            return None

    class Meta:
        verbose_name = "Convocatoria Editorial & Fomento"
        verbose_name_plural = "Convocatorias Editorial & Fomento"
        ordering = ['-created']

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course,
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])
    created = models.DateField(auto_now_add=True,null=True,blank=True)

    class Meta:
            ordering = ['order']

    def __str__(self):
        return '{}. {}'.format(self.order, self.title)


class Content(models.Model):
    module = models.ForeignKey(Module,
                               related_name='contents',
                               on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType,
                                     limit_choices_to={'model__in':('text',
                                                                    'video',
                                                                    'image',
                                                                    'file')},
                                     on_delete=models.CASCADE)
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = OrderField(blank=True, for_fields=['module'])

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

    def render(self):
        return render_to_string('courses/content/{}.html'.format(
            self._meta.model_name), {'item': self})


class Text(ItemBase):
    content = models.TextField()

class File(ItemBase):
    file = models.FileField(upload_to='files')

class Image(ItemBase):
       file = models.FileField(upload_to='images')

class Video(ItemBase):
    url = models.URLField()
