from django import forms
from django.contrib.auth.models import User
from .models import Profile, contacto,contacto_legal, legal,activity,terms
from ckeditor.widgets import CKEditorWidget
from phonenumber_field.formfields import PhoneNumberField



class BooleanWidget(forms.widgets.Widget):
    def __init__(self, attrs=None, check_test=None):
        super().__init__(attrs)
        self.check_test = check_test

    def is_hidden(self, value):
        if self.check_test is None:
            return False
        return not self.check_test(value)

    def render(self, name, value, attrs=None, renderer=None):
        if value is None:
            value = False
        final_attrs = self.build_attrs(attrs, type='checkbox', name=name)
        if self.is_hidden(value):
            final_attrs['style'] = 'display:none'
        if value:
            final_attrs['checked'] = True
        checkbox = '<input class="form-check-input" type="checkbox" role="switch" id="flexSwitchCheckWarning"%s />' % forms.widgets.flatatt(final_attrs)
        label = 'Sí' if value else 'No'
        return forms.widgets.format_html('{} <label for="{}">{}</label>', checkbox, final_attrs['id'], label)
    
class CustomSwitchWidget(forms.widgets.CheckboxInput):
    def __init__(self, attrs=None, checked=False):
        super().__init__(attrs)
        self.checked = checked

    def render(self, name, value, attrs=None, renderer=None):
        final_attrs = dict(attrs, type='checkbox', name=name)  # Añadimos el atributo 'type' directamente
        if self.checked:
            final_attrs['checked'] = True
        return forms.widgets.CheckboxInput().render(name, value, final_attrs, renderer)
    
class LoginForm(forms.Form):
    username = forms.CharField()
    password = forms.CharField(widget=forms.PasswordInput)


class UserRegistrationForm(forms.ModelForm):
    password = forms.CharField(label='Password',
                               widget=forms.PasswordInput)
    password2 = forms.CharField(label='Repeat password',
                                widget=forms.PasswordInput)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'email')

    def clean_password2(self):
        cd = self.cleaned_data
        if cd['password'] != cd['password2']:
            raise forms.ValidationError('Passwords don\'t match.')
        return cd['password2']


class UserEditForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ('username','first_name', 'last_name', 'email')


class ProfileEditForm(forms.ModelForm):
    class Meta:
        model = Profile
        fields = ('photo','fecha_nacimiento','numero_cedula','dactilar','nacionalidad','seudonimo','autoidenty_etnica','genero')
        widgets = {
            'fecha_nacimiento' : forms.DateInput(attrs={'type': 'date'}),
            'numero_cedula' : forms.TextInput(attrs={'placeholder': 'Escriba su número de cedula sin separaciones'}),
            'nacionalidad' : forms.TextInput(attrs={'placeholder': 'Escriba su nacionalidad'}),
           
        }

class ContactEditForm(forms.ModelForm):
    class Meta:
        model = contacto
        fields = ('__all__')
        widgets = {
            'gero_ref' : forms.TextInput(attrs={'placeholder': 'Escriba una referencia cercana de su domicilio'}),
            'direccion' : forms.TextInput(attrs={'placeholder': 'Escriba su Dirección en la siguiente forma:'}),        
        }
class Contact2EditForm(forms.ModelForm):
    class Meta:
        model = contacto
        fields = ('telefono',)
        widgets = {
            'telefono' : forms.NumberInput(attrs={'placeholder': 'Escriba su número de teléfono fíjo.'}),    
        }

class LegalEditForm(forms.ModelForm):
    
 
    class Meta:
        FAVORITE_COLORS_CHOICES = (
    ('Si', 'Si'),
    ('No', 'No'),
)
        model = legal
        fields = ('natu_juri','ruc','tipo_jury','lucro_jury','activity_jury','numero_cedula','dactilar','nacionalidad','fecha_nacimiento','edad','autoidenty_etnica','genero')
        widgets = {
           # 'lucro_jury' : CustomSwitchWidget(attrs={'class': 'form-check-input form-switch form-check-success'}, checked=True),
            'fecha_nacimiento' : forms.DateInput(attrs={'type': 'date'}),
            'edad': forms.TextInput(attrs={'readonly': 'readonly', 'Disabled':'Disabled'}),
            'ruc' : forms.NumberInput(attrs={'placeholder': 'Escriba su número de registro único de contribuyente'}),  
        }
      


class ContactLegalEditForm(forms.ModelForm):
    class Meta:
        model = contacto_legal
        fields = ('provincia','canton1','parroquia1','direccion','gero_ref',)
        widgets = {
            'gero_ref' : forms.TextInput(attrs={'placeholder': 'Escriba una referencia cercana de su domicilio'}),
            'direccion' : forms.TextInput(attrs={'placeholder': 'Escriba su Dirección en la siguiente forma:'}),        
        }
class ContactLegal2EditForm(forms.ModelForm):
    class Meta:
        model = contacto_legal
        fields = ('telefono',)
        widgets = {
            'telefono' : forms.NumberInput(attrs={'placeholder': 'Escriba su número de teléfono fíjo.'}),    
        }

class ActivityEditForm(forms.ModelForm):
    class Meta:
        model = activity
        fields = ('diciplina','experiencia','cv')

class Activity2EditForm(forms.ModelForm):
    class Meta:
        model = activity
        fields = ('enlace_1','enlace_2','enlace_3','ruac','agremiacion','nombre_agremiacion')

class TermsEditForm(forms.ModelForm):
    class Meta:
        model = terms
        fields = ('agree',)

       
#type="checkbox" role="switch" id="flexSwitchCheckDefault1" checked