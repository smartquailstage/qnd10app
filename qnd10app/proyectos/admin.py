import csv
import xlsxwriter
import datetime
from django.contrib import admin
from .models import Subject, Project, Author,BibliographicReference,Content,jurados,WorkPlan,Content, CV,tematica
from django.contrib.contenttypes.admin import GenericTabularInline
from django.utils.safestring import mark_safe
from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse


def export_to_csv(modeladmin, request, queryset): 
    opts = modeladmin.model._meta 
    response = HttpResponse(content_type='text/csv') 
    response['Content-Disposition'] = 'attachment;' \
        'filename={}.csv'.format(opts.verbose_name) 
    writer = csv.writer(response) 
     
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many] 
    # Write a first row with header information 
    writer.writerow([field.verbose_name for field in fields]) 
    # Write data rows 
    for obj in queryset: 
        data_row = [] 
        for field in fields: 
            value = getattr(obj, field.name) 
            if isinstance(value, datetime.datetime): 
                value = value.strftime('%d/%m/%Y') 
            data_row.append(value) 
        writer.writerow(data_row) 
    return response 
export_to_csv.short_description = 'Export to CSV' 


def export_to_excel(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="{}.xlsx"'.format(opts.verbose_name_plural)

    workbook = xlsxwriter.Workbook(response)
    worksheet = workbook.add_worksheet()

    # Obtener los campos del modelo
    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]

    # Escribir encabezados
    for i, field in enumerate(fields):
        worksheet.write(0, i, field.verbose_name)

    # Escribir datos
    for row_num, obj in enumerate(queryset, start=1):
        for col_num, field in enumerate(fields):
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            worksheet.write(row_num, col_num, str(value))  # Convertir a cadena de texto

    workbook.close()
    return response


def proyecto_pdf(obj):
    return mark_safe('<a href="{}">ver perfil</a>'.format(
        reverse('proyectos:project_pdf', args=[obj.id])))
proyecto_pdf.short_description = 'Imprimir proyecto'

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    verbose_name_plural = "Modulos de Convocatoria" 

@admin.register(tematica)
class tematicaAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    verbose_name_plural = "Temáticas del proyecto" 

class AuthorInline(admin.StackedInline):
    model = Author


class BibliographicReferenceInline(admin.StackedInline):
    model = BibliographicReference

class workplanInline(admin.StackedInline):
    model = WorkPlan


class ReadOnlyAdminMixin:
    # Sobrescribe el método para hacer todos los campos solo de lectura
    def get_readonly_fields(self, request, obj=None):
        if obj:  # Si el objeto ya existe (edición)
            return self.readonly_fields + ('resultado',)  # Agrega 'resultado' a los campos de solo lectura
        return self.readonly_fields 
    
class juradosInline(ReadOnlyAdminMixin,admin.StackedInline):
    model = jurados
    max_num = 3
    extra = 0 

    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['get_owner_full_name','title', 'subject', 'created',proyecto_pdf]
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [BibliographicReferenceInline,AuthorInline,workplanInline,juradosInline]
    verbose_name_plural = "Convocatorias" 

    def get_owner_full_name(self, obj):
        return obj.owner.get_full_name() if obj.owner else ""
    get_owner_full_name.short_description = 'Nombre del coordinador'


class ContentInline(GenericTabularInline):
    model = Content
    extra = 0

class CVAdmin(admin.ModelAdmin):
    list_display = ('title', 'owner', 'created', 'updated')
    search_fields = ('title',)
    inlines = [ContentInline]
    verbose_name = "Curriculums de autores"

admin.site.register(CV, CVAdmin)

