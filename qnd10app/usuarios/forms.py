from django import forms
from django.contrib.auth.models import User, Group
from .models import Profile,edit_contact2,edit_contact1, Contacts ,Legal,Activity,DeclaracionVeracidad
from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
#from django.contrib.admin.widgets import AdminDateWidget
from django.forms.fields import DateField
from django.forms import DateInput

class LoginForm(forms.Form):
    username = forms.CharField(label="Nombre de Usuario")
    password = forms.CharField(widget=forms.PasswordInput,label="Contraseña")



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
        fields = ('first_name', 'last_name', 'email')

class UserEditForm2(forms.ModelForm):
    class Meta:
        model = Group
        fields = ('name',)


class DateInput(forms.DateInput):
    input_type = "date"

class ProfileEditForm(forms.ModelForm):


    class Meta:
        model = Profile
        fields = ('activity', 'date_of_birth', 'photo', 'nacionalidad', 'autoidentificacion', 'genero')
        widgets = {
            'date_of_birth': DateInput(
                
            ),
        }


class ContactForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ( 'pais_residencias',)

class Contact1EditForm(forms.ModelForm):
    class Meta:
        model =Contacts
        fields = ('provincia_cantones_ecuador',)

class Contact2EditForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ('parroquia_quito','telefono', 'direccion', 'georeferenciacion', 'perfil_redes_sociales',)

class Contact3EditForm(forms.ModelForm):
    class Meta:
        model = Contacts
        fields = ('telefono', 'direccion', 'georeferenciacion', 'perfil_redes_sociales',)





class LegalEditForm(forms.ModelForm):
    class Meta:
        model = Legal
        fields = ('ruc', 'tipo_personeria')

class Legal2EditForm(forms.ModelForm):
    class Meta:
        model = Legal
        fields = ('categoria_personeria','fines_lucro','actividad_principal', 'representante_legal_nombre', 'representante_legal_apellido', 'representante_legal_cedula', 'telefono_contacto','direccion_domicilio','georeferencia', 'pagina_web')


class ActivityEditForm(forms.ModelForm):
    class Meta:
        model = Activity
        fields = ('disciplina_artistica','experiencia_ambito_cultural','portafolio', 'registro_ruac', 'pertenece_agremiacion_colectivo', 'nombre_agremiacion')

class DeclaratoriaEditForm(forms.ModelForm):
    class Meta:
        model = DeclaracionVeracidad
        fields = ('acepta_terminos_condiciones',)


