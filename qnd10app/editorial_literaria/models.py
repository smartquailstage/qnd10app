from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Modulos de Convocatoria" 

    def __str__(self):
        return self.title


class Course(models.Model):
    owner = models.ForeignKey(User,
                              related_name='courses_created',
                              on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject,
                                related_name='courses',
                                on_delete=models.CASCADE)
    portada = models.ImageField(upload_to='portada/%Y/%m/%d/', blank=True, verbose_name="Foto de portada de convocatoria")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)
    students = models.ManyToManyField(User,
                                      related_name='courses_joined',
                                      blank=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = "Convocatorias" 

    def __str__(self):
        return self.title


class Module(models.Model):
    course = models.ForeignKey(Course,
                               related_name='modules',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['course'])

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


#Manuales de uso
TYPE = [
        ('Crear Convocatoria', 'Crear Convocatoria'),
        ('Editar Convocatoria', 'Editar Convocatoria'),
        ('Mis Convocatorias', 'Mis Convocatorias'),
        ('inscripción', 'inscripción'),
        ('Mis Postulaciones', 'Mis Postulaciones'),
        ('Crear Proyecto', 'Crear Proyecto'),
        ('Editar Proyecto', 'Editar Proyecto'),
        ('Mis Proyectos', 'Mis Proyectos'),
    ]
class ManualCreateConvocatoria(models.Model):
     type = models.CharField(max_length=100, choices=TYPE, verbose_name="Selecione el tipo de manual")
     titulo = models.CharField(max_length=100)
     informacion_basica = RichTextField()
     bloque_1 = RichTextField(blank=True, null=True)
     image_1 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_2 = RichTextField(blank=True, null=True)
     image_2 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_3 = RichTextField(blank=True, null=True)
     image_3 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_4 = RichTextField(blank=True, null=True)
     image_4 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_5 = RichTextField(blank=True, null=True)
     image_5 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     link = models.URLField()


     def __str__(self):
        return self.type


class ManualEditConvocatoria(models.Model):
     type = models.CharField(max_length=100, choices=TYPE, verbose_name="Selecione el tipo de manual")
     titulo = models.CharField(max_length=100)
     informacion_basica = RichTextField()
     bloque_1 = RichTextField(blank=True, null=True)
     image_1 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_2 = RichTextField(blank=True, null=True)
     image_2 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_3 = RichTextField(blank=True, null=True)
     image_3 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_4 = RichTextField(blank=True, null=True)
     image_4 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_5 = RichTextField(blank=True, null=True)
     image_5 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     link = models.URLField()


     def __str__(self):
        return self.type

class ManualMisConvocatoria(models.Model):
     type = models.CharField(max_length=100, choices=TYPE, verbose_name="Selecione el tipo de manual")
     titulo = models.CharField(max_length=100)
     informacion_basica = RichTextField()
     bloque_1 = RichTextField(blank=True, null=True)
     image_1 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_2 = RichTextField(blank=True, null=True)
     image_2 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_3 = RichTextField(blank=True, null=True)
     image_3 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_4 = RichTextField(blank=True, null=True)
     image_4 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_5 = RichTextField(blank=True, null=True)
     image_5 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     link = models.URLField()


     def __str__(self):
        return self.type

class ManualInscripcion(models.Model):
     type = models.CharField(max_length=100, choices=TYPE, verbose_name="Selecione el tipo de manual")
     titulo = models.CharField(max_length=100)
     informacion_basica = RichTextField()
     bloque_1 = RichTextField(blank=True, null=True)
     image_1 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_2 = RichTextField(blank=True, null=True)
     image_2 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_3 = RichTextField(blank=True, null=True)
     image_3 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_4 = RichTextField(blank=True, null=True)
     image_4 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_5 = RichTextField(blank=True, null=True)
     image_5 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     link = models.URLField()

     def __str__(self):
        return self.type



class ManualPostulacion(models.Model):
     type = models.CharField(max_length=100, choices=TYPE, verbose_name="Selecione el tipo de manual")
     titulo = models.CharField(max_length=100)
     informacion_basica = RichTextField()
     bloque_1 = RichTextField(blank=True, null=True)
     image_1 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_2 = RichTextField(blank=True, null=True)
     image_2 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_3 = RichTextField(blank=True, null=True)
     image_3 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_4 = RichTextField(blank=True, null=True)
     image_4 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_5 = RichTextField(blank=True, null=True)
     image_5 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     link = models.URLField()


     def __str__(self):
        return self.type
class ManualMisPostulaciones(models.Model):
     type = models.CharField(max_length=100, choices=TYPE, verbose_name="Selecione el tipo de manual")
     titulo = models.CharField(max_length=100)
     informacion_basica = RichTextField()
     bloque_1 = RichTextField(blank=True, null=True)
     image_1 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_2 = RichTextField(blank=True, null=True)
     image_2 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_3 = RichTextField(blank=True, null=True)
     image_3 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_4 = RichTextField(blank=True, null=True)
     image_4 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_5 = RichTextField(blank=True, null=True)
     image_5 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     link = models.URLField()


     def __str__(self):
        return self.type

class ManualCrearProyecto(models.Model):
     type = models.CharField(max_length=100, choices=TYPE, verbose_name="Selecione el tipo de manual")
     titulo = models.CharField(max_length=100)
     informacion_basica = RichTextField()
     bloque_1 = RichTextField(blank=True, null=True)
     image_1 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_2 = RichTextField(blank=True, null=True)
     image_2 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_3 = RichTextField(blank=True, null=True)
     image_3 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_4 = RichTextField(blank=True, null=True)
     image_4 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_5 = RichTextField(blank=True, null=True)
     image_5 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     link = models.URLField()


     def __str__(self):
        return self.type

class ManualEditProyecto(models.Model):
     type = models.CharField(max_length=100, choices=TYPE, verbose_name="Selecione el tipo de manual")
     titulo = models.CharField(max_length=100)
     informacion_basica = RichTextField()
     bloque_1 = RichTextField(blank=True, null=True)
     image_1 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_2 = RichTextField(blank=True, null=True)
     image_2 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_3 = RichTextField(blank=True, null=True)
     image_3 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_4 = RichTextField(blank=True, null=True)
     image_4 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_5 = RichTextField(blank=True, null=True)
     image_5 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     link = models.URLField()


     def __str__(self):
        return self.type

class ManualMisProyectos(models.Model):
     type = models.CharField(max_length=100, choices=TYPE, verbose_name="Selecione el tipo de manual")
     titulo = models.CharField(max_length=100)
     informacion_basica = RichTextField()
     bloque_1 = RichTextField(blank=True, null=True)
     image_1 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_2 = RichTextField(blank=True, null=True)
     image_2 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_3 = RichTextField(blank=True, null=True)
     image_3 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_4 = RichTextField(blank=True, null=True)
     image_4 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     bloque_5 = RichTextField(blank=True, null=True)
     image_5 = models.ImageField(upload_to='manuales/%Y/%m/%d/', blank=True, null=True, verbose_name="Seleccione una imagen")
     link = models.URLField()


     def __str__(self):
        return self.type


     