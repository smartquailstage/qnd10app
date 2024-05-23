from django import forms
from django.forms.models import inlineformset_factory
from .models import Project, Author, BibliographicReference,WorkPlan


ModuleFormSet = inlineformset_factory(Project,
                                      Author,
                                      fields=['title', 'description'],
                                      extra=2,
                                      can_delete=True)
class CourseEnrollForm(forms.Form):
    project = forms.ModelChoiceField(queryset=Project.objects.all(),
                                    widget=forms.HiddenInput)
    

class BiblioProjectForm(forms.ModelForm):
    class Meta:
        model = BibliographicReference
        fields = ['title', 'authors', 'publication_year', 'journal', 'volume', 'issue', 'pages', 'doi', 'url', 'abstract']

BiblioProjectFormSet = inlineformset_factory(
    parent_model=Project,  # Modelo principal
    model=BibliographicReference,  # Modelo secundario
    form=BiblioProjectForm,  # Formulario a utilizar
    extra=1,  # Número de formularios adicionales que se muestran
    can_delete=True,  # Permite eliminar formularios
    min_num=1,  # Número mínimo de formularios requeridos
    validate_min=True,  # Valida el número mínimo de formularios
    max_num=10,  # Número máximo de formularios permitidos
    validate_max=True,  # Valida el número máximo de formularios
)

class WorkPlanForm(forms.ModelForm):
    class Meta:
        model = WorkPlan
        fields = ['title', 'description', 'start_date', 'end_date']

WorkPlanProjectFormSet = inlineformset_factory(
    parent_model=Project,  # Modelo principal
    model=WorkPlan,  # Modelo secundario
    form=WorkPlanForm,  # Formulario a utilizar
    extra=1,  # Número de formularios adicionales que se muestran
    can_delete=True,  # Permite eliminar formularios
    min_num=1,  # Número mínimo de formularios requeridos
    validate_min=True,  # Valida el número mínimo de formularios
    max_num=10,  # Número máximo de formularios permitidos
    validate_max=True,  # Valida el número máximo de formularios
)
