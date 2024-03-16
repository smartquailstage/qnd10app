from django.contrib import admin
from .models import Categoria_linea_fomento_editorial,announ_linea_fomento_editorial, bases_linea_fomento_editorial,Categorias_linea_fomento_editorial,postulantes


@admin.register(Categoria_linea_fomento_editorial)
class Categoria_linea_fomento_editorialAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}

@admin.register(Categorias_linea_fomento_editorial)
class Categorias_linea_fomento_editorialAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}


class bases_linea_fomento_editorial_Inline(admin.StackedInline):
    model = bases_linea_fomento_editorial


@admin.register(announ_linea_fomento_editorial)
class announ_linea_fomento_editorialAdmin(admin.ModelAdmin):
    list_display = ['title', 'fomento', 'created']
    list_filter = ['created', 'fomento']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [bases_linea_fomento_editorial_Inline]

@admin.register(postulantes)
class postulantesAdmin(admin.ModelAdmin):
    list_display = ['title', 'owner']
