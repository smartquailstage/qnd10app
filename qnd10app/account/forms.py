from django import forms
from django.contrib.auth.models import User
from .models import Profile, contacto,contacto_legal, legal,activity,terms,Contact_Profile,Contact_Profile
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

class ContactProfileForm(forms.ModelForm):
     class Meta:
        model = Profile
        fields = ('photo','fecha_nacimiento','numero_cedula','dactilar','nacionalidad','seudonimo','autoidenty_etnica','genero')
        widgets = {
            'fecha_nacimiento' : forms.DateInput(attrs={'type': 'date'}),
            'numero_cedula' : forms.TextInput(attrs={'placeholder': 'Escriba su número de cedula sin separaciones'}),
            'nacionalidad' : forms.TextInput(attrs={'placeholder': 'Escriba su nacionalidad'}),
           
        }

class ContactEditForm(forms.ModelForm):

    PROVINCIA_CHOICES = [
        ('1','Azuay'),
        ('Bolívar','Bolívar'),
        ('Cañar','Cañar'),
        ('Carchi','Carchi'),
        ('Chimborazo','Chimborazo'),
        ('Cotopaxi','Cotopaxi'),
        ('Esmeraldas','Esmeraldas'),
        ('Galápagos','Galápagos'),
        ('Guayas','Guayas'),
        ('Imbabura','Imbabura'),
        ('Loja','Loja'),
        ('Los Ríos','Los Ríos'),
        ('Manabí','Manabí'),
        ('Morona Santiago','Morona Santiago'),
        ('Napo','Napo'),
        ('Orellana','Orellana'),
        ('Pastaza','Pastaza'),
        ('Pichincha','Pichincha'),
        ('Santa Elena','Santa Elena'),
        ('Santo Domingo de los Tsáchilas','Santo Domingo de los Tsáchilas'),
        ('Sucumbíos','Sucumbíos'),
        ('Tungurahua','Tungurahua'),
        ('Zamora Chinchipe','Zamora Chinchipe'),
    ]

    CANTONES_AZUAY = (
        ('Cuenca', 'Cuenca'),
        ('Chordeleg', 'Chordeleg'),
        ('El Pan', 'El Pan'),
        ('Girón', 'Girón'),
        ('Guachapala', 'Guachapala'),
        ('Gualaceo', 'Gualaceo'),
        ('Nabón', 'Nabón'),
        ('Oña', 'Oña'),
        ('Paute', 'Paute'),
        ('Pucará', 'Pucará'),
        ('San Fernando', 'San Fernando'),
        ('Santa Isabel', 'Santa Isabel'),
        ('Sevilla de Oro', 'Sevilla de Oro'),
        ('Sígsig', 'Sígsig'),
        ('Camilo Ponce Enríquez', 'Camilo Ponce Enríquez'),
    )

    PARROQUIAS_AZUAY = (
        ('Aguarongo', 'Aguarongo'),
        ('Bulán (Jorge Andrade)', 'Bulán (Jorge Andrade)'),
        ('El Carmen del Pongo', 'El Carmen del Pongo'),
        ('El Sagrario', 'El Sagrario'),
        ('El Vecino', 'El Vecino'),
        ('Gil Ramírez Dávalos (Las Juntas)', 'Gil Ramírez Dávalos (Las Juntas)'),
        ('Huertas', 'Huertas'),
        ('Javier Loyola (Chuquipata)', 'Javier Loyola (Chuquipata)'),
        ('Luis Cordero Vega (Cuenca)', 'Luis Cordero Vega (Cuenca)'),
        ('Monay', 'Monay'),
        ('Octavio Cordero Palacios (Santa Rosa)', 'Octavio Cordero Palacios (Santa Rosa)'),
        ('Paccha', 'Paccha'),
        ('Quingeo', 'Quingeo'),
        ('Ricaurte', 'Ricaurte'),
        ('San Blas', 'San Blas'),
        ('San Joaquín', 'San Joaquín'),
        ('San José de Raranga', 'San José de Raranga'),
        ('San Roque', 'San Roque'),
        ('Santiago de Mendez', 'Santiago de Mendez'),
        ('Sayausí', 'Sayausí'),
        ('Sinincay', 'Sinincay'),
        ('Tarqui', 'Tarqui'),
        ('Turi', 'Turi'),
        ('Valle', 'Valle'),
        ('Victoria del Portete (Irquis)', 'Victoria del Portete (Irquis)'),
        ('Zhucay', 'Zhucay'),
    )

    CANTONES_PICHINCHA = (
        ('Quito', 'Quito'),
        ('Cayambe', 'Cayambe'),
        ('Mejía', 'Mejía'),
        ('Pedro Moncayo', 'Pedro Moncayo'),
        ('Rumiñahui', 'Rumiñahui'),
        ('San Miguel de los Bancos', 'San Miguel de los Bancos'),
        ('Pedro Vicente Maldonado', 'Pedro Vicente Maldonado'),
        ('Puerto Quito', 'Puerto Quito'),
    )

    PARROQUIAS_PICHINCHA = (
        ('Carapungo', 'Carapungo'),
        ('San Antonio de Pichincha', 'San Antonio de Pichincha'),
        ('Calderón', 'Calderón'),
        ('San José de Minas', 'San José de Minas'),
        ('Pomasqui', 'Pomasqui'),
        ('Quito', 'Quito'),
        ('Nayón', 'Nayón'),
        ('Cumbayá', 'Cumbayá'),
        ('Tumbaco', 'Tumbaco'),
        ('Pifo', 'Pifo'),
        ('Puembo', 'Puembo'),
        ('Guangopolo', 'Guangopolo'),
        ('Tababela', 'Tababela'),
        ('Yaruquí', 'Yaruquí'),
        ('Alangasí', 'Alangasí'),
        ('Pintag', 'Pintag'),
        ('Conocoto', 'Conocoto'),
        ('Chillogallo', 'Chillogallo'),
        ('Guamaní', 'Guamaní'),
        ('La Ecuatoriana', 'La Ecuatoriana'),
        ('La Mena', 'La Mena'),
        ('Quitumbe', 'Quitumbe'),
        ('Turubamba', 'Turubamba'),
        ('Chilibulo', 'Chilibulo'),
        ('Guangalá', 'Guangalá'),
        ('La Argelia', 'La Argelia'),
        ('La Ferroviaria', 'La Ferroviaria'),
        ('La Libertad', 'La Libertad'),
        ('Lloa', 'Lloa'),
        ('Mindo', 'Mindo'),
        ('Nanegal', 'Nanegal'),
        ('Nanegalito', 'Nanegalito'),
        ('Nayón', 'Nayón'),
        ('Nono', 'Nono'),
        ('Pacto', 'Pacto'),
        ('Pedro Vicente Maldonado', 'Pedro Vicente Maldonado'),
        ('Perucho', 'Perucho'),
        ('Puerto Quito', 'Puerto Quito'),
        ('Puembo', 'Puembo'),
        ('San Antonio', 'San Antonio'),
        ('San José de Minas', 'San José de Minas'),
        ('Tababela', 'Tababela'),
        ('Tambillo', 'Tambillo'),
        ('Tumbaco', 'Tumbaco'),
        ('Yaruquí', 'Yaruquí'),
    )

    provincia = forms.ChoiceField(choices=PROVINCIA_CHOICES, widget=forms.Select(attrs={'id': 'provincia_select'}))
    canton = forms.ChoiceField(choices=CANTONES_AZUAY, required=False, widget=forms.Select(attrs={'id': 'canton_select'}))
    canton1 = forms.ChoiceField(choices=CANTONES_PICHINCHA, required=False, widget=forms.Select(attrs={'id': 'canton1_select'}))
    parroquia = forms.ChoiceField(choices=PARROQUIAS_AZUAY, required=False, widget=forms.Select(attrs={'id': 'parroquia_select'}))
    parroquia1 = forms.ChoiceField(choices=PARROQUIAS_PICHINCHA, required=False, widget=forms.Select(attrs={'id': 'parroquia1_select'}))

    class Meta:
        model = Contact_Profile
        fields = ('provincia', 'canton', 'canton1', 'parroquia', 'parroquia1')

    def __init__(self, *args, **kwargs):
        super(ContactEditForm, self).__init__(*args, **kwargs)
        self.fields['canton'].widget.attrs['style'] = 'display:none'
        self.fields['canton1'].widget.attrs['style'] = 'display:none'
        self.fields['parroquia'].widget.attrs['style'] = 'display:none'
        self.fields['parroquia1'].widget.attrs['style'] = 'display:none'
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
        fields = ('natu_juri','ruc')
        widgets = {
           # 'lucro_jury' : CustomSwitchWidget(attrs={'class': 'form-check-input form-switch form-check-success'}, checked=True),
            'ruc' : forms.NumberInput(attrs={'placeholder': 'Escriba su número de registro único de contribuyente'}),  
        }

class LegalEdit2Form(forms.ModelForm): 
    class Meta:
        model = legal
        fields = ('tipo_jury','lucro_jury','activity_jury','numero_cedula','dactilar','nacionalidad','fecha_nacimiento','edad','autoidenty_etnica','genero')
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