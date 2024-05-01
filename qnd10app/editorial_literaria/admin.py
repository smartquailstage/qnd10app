from django.contrib import admin
from .models import Subject, Course, Module, ManualCreateConvocatoria, ManualEditConvocatoria, ManualInscripcion


@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    verbose_name_plural = "Modulos de Convocatoria" 


class ModuleInline(admin.StackedInline):
    model = Module
    


@admin.register(Course)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [ModuleInline]
    verbose_name_plural = "Convocatorias" 

@admin.register(ManualCreateConvocatoria)
class ManualCreateConvocatoriaAdmin(admin.ModelAdmin):
    list_display = ['type', 'titulo']

@admin.register(ManualEditConvocatoria)
class ManualEditConvocatoriaAdmin(admin.ModelAdmin):
    list_display = ['type', 'titulo']

@admin.register(ManualInscripcion)
class ManualInscripcionAdmin(admin.ModelAdmin):
    list_display = ['type', 'titulo']
