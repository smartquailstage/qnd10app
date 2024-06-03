from django import forms
from django.forms.models import inlineformset_factory
from .models import Course, Module
from django.contrib.auth.models import User


ModuleFormSet = inlineformset_factory(Course,
                                      Module,
                                      fields=('title', 'description'),
                                      extra=2,
                                      can_delete=True)
class CourseEnrollForm(forms.Form):
    course = forms.ModelChoiceField(queryset=Course.objects.all(),
                                    widget=forms.HiddenInput)
    

class ProjectEnrollForm(forms.Form):
      accept = forms.BooleanField(label ="Declara haber leido las bases técnicas.")
      usuario = forms.ModelChoiceField(queryset=User.objects.all(), label="Usuario", disabled=True)
