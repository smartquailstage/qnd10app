from django.contrib import admin
from .models import Subject, Project, Author,BibliographicReference,Content

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    verbose_name_plural = "Modulos de Convocatoria" 

class AuthorInline(admin.StackedInline):
    model = Author


class BibliographicReferenceInline(admin.StackedInline):
    model = BibliographicReference

    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [BibliographicReferenceInline,AuthorInline]
    verbose_name_plural = "Convocatorias" 