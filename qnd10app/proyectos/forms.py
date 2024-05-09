from django import forms
from django.forms.models import inlineformset_factory
from .models import Project, Author, BibliographicReference


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
        fields = ('title', 'authors', 'publication_year','publication_year', 'journal','volume','issue', 'pages','doi','url','abstract')