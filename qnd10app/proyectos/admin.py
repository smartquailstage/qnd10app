from django.contrib import admin
from .models import Subject, Project, Author

@admin.register(Subject)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'slug']
    prepopulated_fields = {'slug': ('title',)}
    verbose_name_plural = "Modulos de Convocatoria" 

class AuthorInline(admin.StackedInline):
    model = Author
    
@admin.register(Project)
class ProjectAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [AuthorInline]
    verbose_name_plural = "Convocatorias" 