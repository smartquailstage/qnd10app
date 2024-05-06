from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from django.utils import timezone


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categorias Literarias"

    def __str__(self):
        return self.title


class Project(models.Model):
    owner = models.ForeignKey(User, related_name='projects_created', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='projects', on_delete=models.CASCADE)
    portada = models.ImageField(upload_to='portada/%Y/%m/%d/', blank=True, verbose_name="Foto de portada de convocatoria")
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField()
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = "Proyectos editoriales postulados"

    def __str__(self):
        return self.title


class Author(models.Model):
    project = models.ForeignKey(Project, related_name='authors', on_delete=models.CASCADE)
    title = models.CharField(max_length=200)
    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['project'])

    class Meta:
        ordering = ['order']

    def __str__(self):
        return '{}. {}'.format(self.order, self.title)


class Content(models.Model):
    author = models.ForeignKey(Author, related_name='authors_contents', on_delete=models.CASCADE)
    content_type = models.ForeignKey(ContentType, limit_choices_to={'model__in': ('file',)}, on_delete=models.CASCADE, related_name='%(app_label)s_%(class)s_content_set')
    object_id = models.PositiveIntegerField()
    item = GenericForeignKey('content_type', 'object_id')
    order = models.IntegerField(default=0)

    class Meta:
        ordering = ['order']


class ItemBase(models.Model):
    owner = models.ForeignKey(User, related_name='%(class)s_related', on_delete=models.CASCADE)
    title = models.CharField(max_length=250)
    created = models.DateTimeField(default=timezone.now)
    updated = models.DateTimeField(auto_now=True)

    class Meta:
        abstract = True

    def __str__(self):
        return self.title

    def render(self):
        return render_to_string('projects/content/{}.html'.format(self._meta.model_name), {'item': self})


class File(ItemBase):
    archivo = models.FileField(upload_to='files')
    # Cambia 'file_related' a 'proyectos_file_related'
    owner = models.ForeignKey(User, related_name='proyectos_file_related', on_delete=models.CASCADE)
