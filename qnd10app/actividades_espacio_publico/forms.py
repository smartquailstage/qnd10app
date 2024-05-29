from django import forms
from .models import Evento

from .models import Evento_30000,Evento_20000,Evento_10000,Evento_5000, Subject

class Evento30000Form(forms.ModelForm):
    class Meta:
        model = Evento_30000
        fields = '__all__'

class Evento20000Form(forms.ModelForm):
    class Meta:
        model = Evento_20000
        fields = '__all__'

class Evento10000Form(forms.ModelForm):
    class Meta:
        model = Evento_10000
        fields = '__all__'

class Evento5000Form(forms.ModelForm):
    class Meta:
        model = Evento_5000
        fields = '__all__'


class SubjectEvento(forms.ModelForm):
    class Meta:
        model = Subject
        fields = '__all__'


