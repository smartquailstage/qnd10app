import csv
import xlsxwriter
import datetime
from django.contrib import admin
from .models import  Subject,Evento_30000,Evento_20000,Evento_10000,Evento_5000
from django.utils.safestring import mark_safe
from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse

admin.site.register(Subject)

admin.site.register(Evento_20000)
admin.site.register(Evento_10000)
admin.site.register(Evento_5000)


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


def evento_pdf(obj):
    return mark_safe('<a href="{}">ver perfil</a>'.format(
        reverse('actividades_espacio_publico:admin_evento_30000_pdf', args=[obj.id])))
evento_pdf.short_description = 'Perfil de usuario en evento'

@admin.register(Evento_30000)
class Evento_30000Admin(admin.ModelAdmin):
    list_display = ['get_user_full_name', 'servicios_artisticos','rider_tecnico', 'aforo', evento_pdf]
    actions = [ export_to_csv, export_to_excel]
    verbose_name = "Información de Evento 30000"
    verbose_name_plural = "Información de Evento 30000"

    def get_user_full_name(self, obj):
        return obj.user.get_full_name()
    get_user_full_name.short_description = 'Usuario'