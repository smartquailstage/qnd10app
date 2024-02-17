from django.contrib import admin
from .models import ConvName, Convocatoria, Bases


@admin.register(ConvName)
class SubjectAdmin(admin.ModelAdmin):
    list_display = ['nombre', 'slug']
    prepopulated_fields = {'slug': ('nombre',)}


class BasesInline(admin.StackedInline):
    model = Bases


@admin.register(Convocatoria)
class CourseAdmin(admin.ModelAdmin):
    list_display = ['title', 'subject', 'created']
    list_filter = ['created', 'subject']
    search_fields = ['title', 'overview']
    prepopulated_fields = {'slug': ('title',)}
    inlines = [BasesInline]