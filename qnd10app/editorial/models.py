from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from ckeditor.fields import RichTextField


class ConvName(models.Model):
    nombre = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['nombre']

    def __str__(self):
        return self.nombre


class Convocatoria(models.Model):
    user_name = models.ForeignKey(User,
                              related_name='courses_created',
                              on_delete=models.CASCADE,verbose_name='Nombre de Usuario')
    subject = models.ForeignKey(ConvName,
                                related_name='courses',
                                on_delete=models.CASCADE,verbose_name='Nombre de Convocatoria')
    title = models.CharField(max_length=200,verbose_name='Título de Convocatoria')
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField(verbose_name='Descripción de convocatoria')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']

    def __str__(self):
        return self.title


class Bases(models.Model):
    convocatoria = models.ForeignKey(Convocatoria,
                               related_name='bases',
                               on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True,verbose_name='Descripción de convocatoria')
    order = OrderField(blank=True, for_fields=['convocatorias'])

    class Meta:
            ordering = ['order']

    def __str__(self):
        return '{}. {}'.format(self.order, self.title)


class Content(models.Model):
    base = models.ForeignKey(Bases,
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


class term(models.Model):
     term1 = RichTextField()
     term2 = RichTextField(null=True)
     term3 = RichTextField(null=True)
     term4 = RichTextField(null=True)
     term5 = RichTextField(null=True)
     term6 = RichTextField(null=True)
     term7 = RichTextField(null=True) 


     
