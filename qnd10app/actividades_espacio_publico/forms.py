from django import forms
from .models import Evento

from .models import Evento_30000,Evento_20000,Evento_10000,Evento_5000, Subject

class Evento30000Form(forms.ModelForm):
    class Meta:
        model = Evento_30000
        exclude = ['user']

class Evento20000Form(forms.ModelForm):
    class Meta:
        model = Evento_20000
        exclude = ['user']

class Evento10000Form(forms.ModelForm):
    class Meta:
        model = Evento_10000
        exclude = ['user']

class Evento5000Form(forms.ModelForm):
    class Meta:
        model = Evento_5000
        exclude = ['user']


class SubjectEvento(forms.ModelForm):
    class Meta:
        model = Subject
        exclude = ['user']


