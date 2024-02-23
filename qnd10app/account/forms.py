from django import forms
from django.contrib.auth.models import User
from .models import Profile, contacto,legal
from phonenumber_field.formfields import PhoneNumberField


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
        fields = ('photo','fecha_nacimiento','edad','numero_cedula','dactilar','nacionalidad','seudonimo','autoidenty_etnica','genero')
        widgets = {
            'fecha_nacimiento' : forms.DateInput(attrs={'type': 'date'}),
            'edad': forms.TextInput(attrs={'readonly': 'readonly', 'Disabled':'Disabled'}),
            'numero_cedula' : forms.TextInput(attrs={'placeholder': 'Escriba su número de cedula sin separaciones'}),
            'nacionalidad' : forms.TextInput(attrs={'placeholder': 'Escriba su nacionalidad'}),
           
        }

class ContactEditForm(forms.ModelForm):
    class Meta:
        model = contacto
        fields = ('provincia','canton1','parroquia1','direccion','gero_ref',)
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
        model = legal
        fields = ('natu_juri','ruc',)
        widgets = {
            'ruc' : forms.NumberInput(attrs={'placeholder': 'Escriba su número de registro único de contribuyente'}),  
        }


#type="checkbox" role="switch" id="flexSwitchCheckDefault1" checked