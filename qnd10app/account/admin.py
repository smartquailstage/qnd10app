import csv
import datetime
import xlsxwriter
from django.contrib import admin
from django.http import HttpResponse
from django.urls import reverse
from django.utils.safestring import mark_safe
from django.views.generic import ListView
from .models import Profile,Contact_Profile,legal,contacto_legal,activity,terms,edit_profile_done,Manual_inscripcion



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
export_to_csv.short_description = 'Exportar a formato CSV' 


def export_to_xls(modeladmin, request, queryset):
    opts = modeladmin.model._meta
    response = HttpResponse(content_type='application/vnd.openxmlformats-officedocument.spreadsheetml.sheet')
    response['Content-Disposition'] = 'attachment; filename="{}.xlsx"'.format(opts.verbose_name)

    wb = xlsxwriter.Workbook(response)
    ws = wb.add_worksheet('Sheet1')

    fields = [field for field in opts.get_fields() if not field.many_to_many and not field.one_to_many]
    
    # Escribir fila de encabezado
    for i, field in enumerate(fields):
        ws.write(0, i, field.verbose_name)
    
    # Escribir filas de datos
    for row_num, obj in enumerate(queryset):
        for col_num, field in enumerate(fields):
            value = getattr(obj, field.name)
            if isinstance(value, datetime.datetime):
                value = value.strftime('%d/%m/%Y')
            ws.write(row_num + 1, col_num, str(value))

    wb.close()
    return response

export_to_xls.short_description = 'Exportar a formato XLS'



def profile_pdf(obj):
    return mark_safe('<a href="{}"><i><i class="fa fa-eye"></i></a>'.format(
        reverse('account:admin_profile_pdf', args=[obj.id])))
profile_pdf.short_description = 'Perfil'

def contact_pdf(obj):
    return mark_safe('<a href="{}"><i><i class="fa fa-eye"></i></a>'.format(
        reverse('account:admin_contact_pdf', args=[obj.id])))
contact_pdf.short_description = 'contacto'



def legal_pdf(obj):
    return mark_safe('<a href="{}"><i><i class="fa fa-eye"></i></a>'.format(
        reverse('account:admin_legal_pdf', args=[obj.id])))
legal_pdf.short_description = 'Estatus legal'

def legal_contact_pdf(obj):
    return mark_safe('<a href="{}"><i><i class="fa fa-eye"></i></a>'.format(
        reverse('account:admin_contact_legal_pdf', args=[obj.id])))
legal_contact_pdf.short_description = 'representante legal'

def activity_pdf(obj):
    return mark_safe('<a href="{}"><i><i class="fa fa-eye"></i></a>'.format(
        reverse('account:admin_activity_pdf', args=[obj.id])))
activity_pdf.short_description = 'Actividades culturales'

def terms_pdf(obj):
    return mark_safe('<a href="{}"><i><i class="fa fa-eye"></i></a>'.format(
        reverse('account:admin_terms_pdf', args=[obj.id])))
terms_pdf.short_description = 'Declaratoria'

def whatsapp(obj):
     return mark_safe('<a href="https://api.whatsapp.com/send?phone={}"><i><i class="fa fa-phone"></i></a>'.format(obj.telefono))
whatsapp.short_description = 'Whatsapp'

def email(obj):
     return mark_safe('<a href="mailto:{}" target="_blank" ><i class="fa fa-envelope"></i></a>'.format(obj.user.email))
whatsapp.short_description = 'Enviar correo'



# Definición del Modelo Admin Proxy
class ProfileProxyAdmin(admin.ModelAdmin):
    # Campos a mostrar en el panel de administración
    list_display = ('user', 'first_name',)

@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['get_full_name', email ,profile_pdf, contact_pdf,legal_pdf,legal_contact_pdf,activity_pdf,terms_pdf]
    verbose_name = 'Información de usuarios'
    verbose_name_plural = 'Información de usuarios'
    proxy = True
    actions = [export_to_csv,export_to_xls]

    def get_full_name(self, obj):
        return obj.user.get_full_name()
    get_full_name.short_description = 'Nombre completo'

@admin.register(Contact_Profile)
class contactoprofileAdmin(admin.ModelAdmin):
    list_display = ['user', 'provincia', 'canton','direccion']
    verbose_name = 'Información de contacto de Postulante'
    verbose_name_plural = 'Información de contactos de Postulantes'
    actions = [export_to_csv,export_to_xls]

@admin.register(legal)
class legalAdmin(admin.ModelAdmin):
    list_display = ['user','ruc','tipo_jury', 'lucro_jury']
    verbose_name = 'Estatus legal de Postulante'
    verbose_name_plural = 'Estatus legal de Postulantes'
    actions = [export_to_csv,export_to_xls]

@admin.register(contacto_legal)
class contacto_legalAdmin(admin.ModelAdmin):
    list_display = ['user', 'provincia', 'canton1','direccion']
    verbose_name = 'contacto de representante legal de Postulante'
    verbose_name_plural = 'contactos de representante legal de Postulantes'
    actions = [export_to_csv,export_to_xls]

@admin.register(activity)
class activityAdmin(admin.ModelAdmin):
    list_display = ['diciplina',]
    verbose_name = 'actividad cultural del Postulante'
    verbose_name_plural = 'actividades culturales del Postulante'
    actions = [export_to_csv,export_to_xls]

@admin.register(terms)
class termsAdmin(admin.ModelAdmin):
    list_display = ['user', 'agree']
    verbose_name = 'Declaratoria de postulante'
    verbose_name_plural = 'Declaratorias de postulantes'
    actions = [export_to_csv,export_to_xls]

@admin.register(edit_profile_done)
class edit_profile_doneAdmin(admin.ModelAdmin):
    list_display = ['nombre_tech', 'telefono','email']
    verbose_name = 'Información de Tecnicos'
    verbose_name_plural = 'Información de Tecnicos'
    actions = [export_to_csv,export_to_xls]

@admin.register(Manual_inscripcion)
class Manual_inscripcionAdmin(admin.ModelAdmin):
    list_display = ['paso1',]
    verbose_name = 'Manual de usuario'
    verbose_name_plural = 'Manual de usuario'