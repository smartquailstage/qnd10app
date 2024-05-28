from django.db import models
from django.contrib.auth.models import User
from django.contrib.contenttypes.models import ContentType
from django.contrib.contenttypes.fields import GenericForeignKey
from .fields import OrderField
from django.template.loader import render_to_string
from django.utils.safestring import mark_safe
from ckeditor.fields import RichTextField
from django.utils import timezone
from editorial_literaria.models import Course


class Subject(models.Model):
    title = models.CharField(max_length=200)
    slug = models.SlugField(max_length=200, unique=True)

    class Meta:
        ordering = ['title']
        verbose_name_plural = "Categorias Literarias"

    def __str__(self):
        return self.title

    
class Project(models.Model):
    PROCESS = (
        ('Aprobado', 'Aprobado'),
        ('Activo', 'Activo'),
        ('Subsanación', 'Subsanación'),
        ('Rechazado', 'Rechazado'),
    )
    
    owner = models.ForeignKey(User, related_name='projects_created', on_delete=models.CASCADE)
    subject = models.ForeignKey(Subject, related_name='proyectos_subject', on_delete=models.CASCADE, verbose_name="Nombre de categoría de convocatoria a la que se desea postular", help_text="Seleccione la categoría de la convocatoria en la que desea postular")
    #portada = models.ImageField(upload_to='portada/%Y/%m/%d/', blank=True, verbose_name="Foto de portada de convocatoria")
    title = models.CharField(max_length=300, verbose_name="Título del proyecto")
    slug = models.SlugField(max_length=200, unique=True)
    overview = models.TextField(verbose_name="Resumen breve del proyecto de tomo", help_text="Identificación de un debate o giro paradigmático y explicación sobre cómo cada uno de los capítulos que compondrán el tomo representan lo dicho.")
    plan = models.TextField(verbose_name="Describa el plan de uso de incentivo", help_text="Detalle de manera clara y sucinta.",null=True,blank=True)
    cv = models.FileField(upload_to='curriculms/',verbose_name="Perfil del postulante", help_text ="En calidad de coordinador/a o autor/a del proyecto, que acredite experiencia en el campo del conocimiento pertinente, así como experiencia en temas editoriales, de publicación, coordinación y/o de curaduría de proyectos culturales o académicos según corresponda, de al menos 2 años.", null=True,blank=True)

    #bibliographic_reference = models.ForeignKey(BibliographicReference, on_delete=models.CASCADE, blank=True, null=True) 
    created = models.DateTimeField(auto_now_add=True)
    course = models.ForeignKey(Course, related_name='proyectos_course', on_delete=models.CASCADE,null=True,blank=True,verbose_name="Elija la convocatoria que desea postular este proyecto.")
    proceso =  models.CharField(max_length=255, blank=True, null=True, verbose_name="Proceso del proyecto postulado", choices=PROCESS, help_text="Elija el proceso en la que se encuentra esta postulacion", default="Activo")
    recomend = RichTextField(help_text="Si el proceso se encuentrta en subsanamiento, Escribir en el re-cuadro, las recomendaciones.", null=True,blank=True)
    dictamen = RichTextField(help_text="Si el proceso se encuentrta en Aprobado y calificado, Escribir en el re-cuadro el dicatmen final de jurado.", null=True,blank=True)

    class Meta:
        ordering = ['-created']
        verbose_name_plural = "Proyectos editoriales postulados"

    def __str__(self):
        return self.title
    
class WorkPlan(models.Model):
    project = models.ForeignKey(Project, related_name='workplan', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=200)
    description = models.TextField()
    start_date = models.DateField()
    end_date = models.DateField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    owner = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.title
    
class BibliographicReference(models.Model):
    project = models.ForeignKey(Project, related_name='biblio', on_delete=models.CASCADE, null=True, blank=True)
    title = models.CharField(max_length=255)
    authors = models.CharField(max_length=255)
    publication_year = models.PositiveIntegerField()
    journal = models.CharField(max_length=255, blank=True, null=True)
    volume = models.CharField(max_length=50, blank=True, null=True)
    issue = models.CharField(max_length=50, blank=True, null=True)
    pages = models.CharField(max_length=50, blank=True, null=True)
    doi = models.CharField(max_length=100, blank=True, null=True)
    url = models.URLField(blank=True, null=True)
    abstract = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.title


class Author(models.Model):
    user = models.ForeignKey(User, related_name='projects_authors', on_delete=models.CASCADE, blank=True,null=True)
    project = models.ForeignKey(Project, related_name='authors', on_delete=models.CASCADE)
    title = models.CharField(max_length=200,verbose_name="Nombre completo de Autor")
   # first_name = models.CharField(max_length=200,null=True,blank=True)
   # last_name = models.CharField(max_length=200,null=True,blank=True)

    description = models.TextField(blank=True)
    order = OrderField(blank=True, for_fields=['project'])

    class Meta:
        ordering = ['order']

    def __str__(self):
        return '{}. {}'.format(self.order, self.title)


class Content(models.Model):
    author = models.ForeignKey(Author, related_name='authors_contents_project', on_delete=models.CASCADE)
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


class CV(ItemBase):
    file = models.FileField(upload_to='files')
    
