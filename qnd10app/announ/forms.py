from django import forms
from django.forms.models import inlineformset_factory
from .models import announ_linea_fomento_editorial, bases_linea_fomento_editorial


ModuleFormSet = inlineformset_factory(announ_linea_fomento_editorial,
                                      bases_linea_fomento_editorial,
                                      fields=['title', 'description',],
                                      extra=2,
                                      can_delete=True)
