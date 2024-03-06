from django.contrib import admin
from .models import Profile,Contact_Profile,legal,contacto_legal,activity,terms,edit_profile_done,Manual_inscripcion


@admin.register(Profile)
class ProfileAdmin(admin.ModelAdmin):
    list_display = ['user', 'numero_cedula', 'nacionalidad','edad', 'genero']
    class Meta:
        verbose_name = 'Perfil de Postulantes'
        verbose_name_plural = 'Perfiles de postulantes'

@admin.register(Contact_Profile)
class contactoprofileAdmin(admin.ModelAdmin):
    list_display = ['user', 'provincia', 'canton','direccion']
    verbose_name = 'Información de contacto de Postulante'
    verbose_name_plural = 'Información de contactos de Postulantes'

@admin.register(legal)
class legalAdmin(admin.ModelAdmin):
    list_display = ['user','ruc','tipo_jury', 'lucro_jury']
    verbose_name = 'Estatus legal de Postulante'
    verbose_name_plural = 'Estatus legal de Postulantes'

@admin.register(contacto_legal)
class contacto_legalAdmin(admin.ModelAdmin):
    list_display = ['user', 'provincia', 'canton1','direccion']
    verbose_name = 'contacto de representante legal de Postulante'
    verbose_name_plural = 'contactos de representante legal de Postulantes'

@admin.register(activity)
class activityAdmin(admin.ModelAdmin):
    list_display = ['diciplina',]
    verbose_name = 'actividad cultural del Postulante'
    verbose_name_plural = 'actividades culturales del Postulante'

@admin.register(terms)
class termsAdmin(admin.ModelAdmin):
    list_display = ['user', 'agree']
    verbose_name = 'Declaratoria de postulante'
    verbose_name_plural = 'Declaratorias de postulantes'

@admin.register(edit_profile_done)
class edit_profile_doneAdmin(admin.ModelAdmin):
    list_display = ['nombre_tech', 'telefono','email']
    verbose_name = 'Información de Tecnicos'
    verbose_name_plural = 'Información de Tecnicos'

@admin.register(Manual_inscripcion)
class Manual_inscripcionAdmin(admin.ModelAdmin):
    list_display = ['paso1',]
    verbose_name = 'Manual de usuario'
    verbose_name_plural = 'Manual de usuario'