from django.db import models
from django.conf import settings
from django_countries.fields import CountryField
from phonenumber_field.modelfields import PhoneNumberField
from localflavor.ec.forms import ECProvinceSelect
from ckeditor.fields import RichTextField
from django.core.cache import cache
from django.contrib.auth.models import User, Group
from django.core.validators import RegexValidator

class Profile(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Nombre de Usuario")
    user_group = models.ForeignKey(Group, on_delete=models.SET_NULL, null=True, blank=True,verbose_name="Tipo de cuenta de Usuario")
    date_of_birth = models.DateField(blank=True, null=True, verbose_name="Fecha de Nacimiento")
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, verbose_name="Foto de Perfil")
    nacionalidad = models.CharField(blank=True, null=True, max_length=100, verbose_name="Nacionalidad")
    autoidentificacion = models.CharField(blank=True, null=True, max_length=3, choices=[("SI", "Sí"), ("NO", "No")], verbose_name="¿Usted pertenece a un pueblo o nacionalidad indígena, montubio o afro-ecuatoriano?",help_text="¿Usted pertenece a un pueblo o nacionalidad indígena, montubio o afro-ecuatoriano?")
    genero = models.CharField(blank=True, null=True, max_length=10, choices=[("MASCULINO", "Masculino"), ("FEMENINO", "Femenino"), ("OTRO", "Otro")], verbose_name="Identidad de Género")
    class Meta:
        ordering = ['user']
        verbose_name_plural = "Perfiles de Usuarios"

    def __str__(self):
        return 'Perfil de Usuario {}'.format(self.user.username)
    
class Contacts(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Nombre de Usuario")
    pais_residencias = CountryField(multiple=True, verbose_name="País de Residencia", blank=True,max_length=150)
    
    PROVINCIAS_CANTONES_CHOICES = (
        ('Azuay', (
                ('Cuenca', 'Cuenca'),
                ('Gualaceo', 'Gualaceo'),
                ('Sígsig', 'Sígsig'),
                ('Chordeleg', 'Chordeleg'),
                ('Sigsig', 'Sigsig'),
                ('Oña', 'Oña'),
                ('Girón', 'Girón'),
                ('Paute', 'Paute'),
                ('Santa Isabel', 'Santa Isabel'),
                ('Nabón', 'Nabón'),
                ('El Pan', 'El Pan'),
                ('Sevilla de Oro', 'Sevilla de Oro'),
                ('Guachapala', 'Guachapala'),
                ('Camilo Ponce Enríquez', 'Camilo Ponce Enríquez'),
                ('Suscal', 'Suscal'),
                ('Pucará', 'Pucará'),
                ('San Fernando', 'San Fernando'),
            )
        ),
        ('Bolívar', (
                ('Guaranda', 'Guaranda'),
                ('Caluma', 'Caluma'),
                ('Chillanes', 'Chillanes'),
                ('Chimbo', 'Chimbo'),
                ('Echeandía', 'Echeandía'),
                ('Las Naves', 'Las Naves'),
            )
        ),
        ('Cañar', (
                ('Azogues', 'Azogues'),
                ('Biblián', 'Biblián'),
                ('Cañar', 'Cañar'),
                ('La Troncal', 'La Troncal'),
                ('Déleg', 'Déleg'),
                ('El Tambo', 'El Tambo'),
                ('Suscal', 'Suscal'),
            )
        ),
        ('Carchi', (
                ('Tulcán', 'Tulcán'),
                ('Bolívar', 'Bolívar'),
                ('Espejo', 'Espejo'),
                ('Mira', 'Mira'),
                ('Montúfar', 'Montúfar'),
                ('San Pedro de Huaca', 'San Pedro de Huaca'),
            )
        ),
        ('Chimborazo', (
                ('Riobamba', 'Riobamba'),
                ('Alausí', 'Alausí'),
                ('Colta', 'Colta'),
                ('Chambo', 'Chambo'),
                ('Chunchi', 'Chunchi'),
                ('Guamote', 'Guamote'),
                ('Guano', 'Guano'),
                ('Pallatanga', 'Pallatanga'),
                ('Penipe', 'Penipe'),
            )
        ),
        ('Cotopaxi', (
                ('Latacunga', 'Latacunga'),
                ('La Maná', 'La Maná'),
                ('Pangua', 'Pangua'),
                ('Pujilí', 'Pujilí'),
                ('Salcedo', 'Salcedo'),
                ('Saquisilí', 'Saquisilí'),
                ('Sigchos', 'Sigchos'),
            )
        ),
        ('El Oro', (
                ('Machala', 'Machala'),
                ('Arenillas', 'Arenillas'),
                ('Atahualpa', 'Atahualpa'),
                ('Balsas', 'Balsas'),
                ('Chilla', 'Chilla'),
                ('El Guabo', 'El Guabo'),
                ('Huaquillas', 'Huaquillas'),
                ('Marcabelí', 'Marcabelí'),
                ('Pasaje', 'Pasaje'),
                ('Piñas', 'Piñas'),
                ('Portovelo', 'Portovelo'),
                ('Santa Rosa', 'Santa Rosa'),
                ('Zaruma', 'Zaruma'),
                ('Las Lajas', 'Las Lajas'),
            )
        ),
        ('Esmeraldas', (
                ('Esmeraldas', 'Esmeraldas'),
                ('Eloy Alfaro', 'Eloy Alfaro'),
                ('Muisne', 'Muisne'),
                ('Quinindé', 'Quinindé'),
                ('San Lorenzo', 'San Lorenzo'),
                ('Atacames', 'Atacames'),
                ('Rioverde', 'Rioverde'),
            )
        ),
        ('Galápagos', (
                ('San Cristóbal', 'San Cristóbal'),
                ('Isabela', 'Isabela'),
                ('Santa Cruz', 'Santa Cruz'),
            )
        ),
        ('Guayas', (
                ('Guayaquil', 'Guayaquil'),
                ('Alfredo Baquerizo Moreno', 'Alfredo Baquerizo Moreno (Juján)'),
                ('Balao', 'Balao'),
                ('Balzar', 'Balzar'),
                ('Colimes', 'Colimes'),
                ('Coronel Marcelino Maridueña', 'Coronel Marcelino Maridueña'),
                ('Daule', 'Daule'),
                ('Durán', 'Durán'),
                ('El Empalme', 'El Empalme'),
                ('El Triunfo', 'El Triunfo'),
                ('Milagro', 'Milagro'),
                ('Naranjal', 'Naranjal'),
                ('Naranjito', 'Naranjito'),
                ('Palestina', 'Palestina'),
                ('Pedro Carbo', 'Pedro Carbo'),
                ('Samborondón', 'Samborondón'),
                ('Santa Lucía', 'Santa Lucía'),
                ('Simón Bolívar', 'Simón Bolívar'),
                ('Yaguachi', 'Yaguachi'),
                ('General Antonio Elizalde (Bucay)', 'General Antonio Elizalde (Bucay)'),
                ('Isidro Ayora', 'Isidro Ayora'),
                ('Lomas de Sargentillo', 'Lomas de Sargentillo'),
                ('Nobol', 'Nobol'),
                ('Santa Elena', 'Santa Elena'),
                ('La Libertad', 'La Libertad'),
                ('Salinas', 'Salinas'),
            )
        ),
        ('Imbabura', (
                ('Ibarra', 'Ibarra'),
                ('Antonio Ante', 'Antonio Ante (Andrade Marin)'),
                ('Cotacachi', 'Cotacachi'),
                ('Otavalo', 'Otavalo'),
                ('Pimampiro', 'Pimampiro'),
                ('San Miguel de Urcuquí', 'San Miguel de Urcuquí'),
            )
        ),
        ('Loja', (
                ('Loja', 'Loja'),
                ('Calvas', 'Calvas'),
                ('Catamayo', 'Catamayo'),
                ('Celica', 'Celica'),
                ('Chaguarpamba', 'Chaguarpamba'),
                ('Espíndola', 'Espíndola'),
                ('Gonzanamá', 'Gonzanamá'),
                ('Macará', 'Macará'),
                ('Paltas', 'Paltas'),
                ('Puyango', 'Puyango'),
                ('Saraguro', 'Saraguro'),
                ('Sozoranga', 'Sozoranga'),
                ('Zapotillo', 'Zapotillo'),
                ('Pindal', 'Pindal'),
                ('Quilanga', 'Quilanga'),
                ('Olmedo', 'Olmedo'),
            )
        ),
        ('Los Ríos', (
                ('Babahoyo', 'Babahoyo'),
                ('Baba', 'Baba'),
                ('Montalvo', 'Montalvo'),
                ('Buena Fe', 'Buena Fe'),
                ('Mocache', 'Mocache'),
                ('Urdaneta', 'Urdaneta'),
                ('Ventanas', 'Ventanas'),
                ('Quevedo', 'Quevedo'),
                ('Quinsaloma', 'Quinsaloma'),
                ('Valencia', 'Valencia'),
                ('Vinces', 'Vinces'),
                ('Palenque', 'Palenque'),
            )
        ),
        ('Manabí', (
                ('Portoviejo', 'Portoviejo'),
                ('Bolívar', 'Bolívar'),
                ('Chone', 'Chone'),
                ('El Carmen', 'El Carmen'),
                ('Flavio Alfaro', 'Flavio Alfaro'),
                ('Jipijapa', 'Jipijapa'),
                ('Junín', 'Junín'),
                ('Manta', 'Manta'),
                ('Montecristi', 'Montecristi'),
                ('Paján', 'Paján'),
                ('Pichincha', 'Pichincha'),
                ('Rocafuerte', 'Rocafuerte'),
                ('Santa Ana', 'Santa Ana'),
                ('Sucre', 'Sucre'),
                ('Tosagua', 'Tosagua'),
                ('24 de Mayo', '24 de Mayo'),
                ('Pedernales', 'Pedernales'),
                ('Olmedo', 'Olmedo'),
                ('Puerto López', 'Puerto López'),
                ('Jama', 'Jama'),
                ('San Vicente', 'San Vicente'),
            )
        ),
        ('Morona Santiago', (
                ('Macas', 'Macas'),
                ('Gualaquiza', 'Gualaquiza'),
                ('Huamboya', 'Huamboya'),
                ('Limón Indanza', 'Limón Indanza'),
                ('Logroño', 'Logroño'),
                ('Morona', 'Morona'),
                ('Pablo Sexto', 'Pablo Sexto'),
                ('Palora', 'Palora'),
                ('San Juan Bosco', 'San Juan Bosco'),
                ('Santiago de Méndez', 'Santiago de Méndez'),
                ('Sucúa', 'Sucúa'),
                ('Taisha', 'Taisha'),
                ('Tiwintza', 'Tiwintza'),
            )
        ),
        ('Napo', (
                ('Tena', 'Tena'),
                ('Archidona', 'Archidona'),
                ('El Chaco', 'El Chaco'),
                ('Quijos', 'Quijos'),
                ('Carlos Julio Arosemena Tola', 'Carlos Julio Arosemena Tola'),
            )
        ),
        ('Orellana', (
                ('Orellana', 'Orellana'),
                ('Aguarico', 'Aguarico'),
                ('La Joya de los Sachas', 'La Joya de los Sachas'),
                ('Loreto', 'Loreto'),
            )
        ),
        ('Pastaza', (
                ('Puyo', 'Puyo'),
                ('Arajuno', 'Arajuno'),
                ('Mera', 'Mera'),
                ('Santa Clara', 'Santa Clara'),
            )
        ),
        ('Pichincha', (
                ('Quito', 'Quito'),
                ('Cayambe', 'Cayambe'),
                ('Mejía', 'Mejía'),
                ('Pedro Moncayo', 'Pedro Moncayo'),
                ('Rumiñahui', 'Rumiñahui'),
                ('San Miguel de los Bancos', 'San Miguel de los Bancos'),
                ('Pedro Vicente Maldonado', 'Pedro Vicente Maldonado'),
                ('Puerto Quito', 'Puerto Quito'),
            )
        ),
        ('Santa Elena', (
                ('Santa Elena', 'Santa Elena'),
                ('La Libertad', 'La Libertad'),
                ('Salinas', 'Salinas'),
            )
        ),
        ('Santo Domingo de los Tsáchilas', (
                ('Santo Domingo', 'Santo Domingo'),
                ('La Concordia', 'La Concordia'),
            )
        ),
        ('Sucumbíos', (
                ('Nueva Loja', 'Nueva Loja'),
                ('Cascales', 'Cascales'),
                ('Cuyabeno', 'Cuyabeno'),
                ('Gonzalo Pizarro', 'Gonzalo Pizarro'),
                ('Putumayo', 'Putumayo'),
                ('Shushufindi', 'Shushufindi'),
                ('Sucumbíos', 'Sucumbíos'),
                ('Lago Agrio', 'Lago Agrio'),
            )
        ),
        ('Tungurahua', (
                ('Ambato', 'Ambato'),
                ('Baños de Agua Santa', 'Baños de Agua Santa'),
                ('Cevallos', 'Cevallos'),
                ('Mocha', 'Mocha'),
                ('Patate', 'Patate'),
                ('Quero', 'Quero'),
                ('San Pedro de Pelileo', 'San Pedro de Pelileo'),
                ('Pelileo', 'Pelileo'),
                ('Pillaro', 'Pillaro'),
                ('Tisaleo', 'Tisaleo'),
            )
        ),
        ('Zamora Chinchipe', (
                ('Zamora', 'Zamora'),
                ('Chinchipe', 'Chinchipe'),
                ('Centinela del Cóndor', 'Centinela del Cóndor'),
                ('Nangaritza', 'Nangaritza'),
                ('Palanda', 'Palanda'),
                ('Paquisha', 'Paquisha'),
                ('Yacuambi', 'Yacuambi'),
                ('Yantzaza', 'Yantzaza'),
                ('El Pangui', 'El Pangui'),
            )
        ),
    )
    
    provincia_cantones_ecuador = models.CharField(max_length=255, blank=True, null=True, verbose_name="Provincia y Cantones", choices=PROVINCIAS_CANTONES_CHOICES, help_text="Si su pais de residencia es Ecuador, Elija una provincia. Caso contrario dejelo en blanco")

    PARROQUIAS_QUITO = (
        ('Conocoto', 'Conocoto'),
        ('Cumbayá', 'Cumbayá'),
        ('Chillogallo', 'Chillogallo'),
        ('Chilibulo', 'Chilibulo'),
        ('Chillos', 'Ch  illos'),
        ('Guamaní', 'Guamaní'),
        ('Calderón', 'Calderón'),
        ('Carapungo', 'Carapungo'),
        ('Pomasqui', 'Pomasqui'),
        ('Nayón', 'Nayón'),
        ('Tumbaco', 'Tumbaco'),
        ('Tababela', 'Tababela'),
        ('Quito', 'Quito'),
    )
    
    parroquia_quito = models.CharField(max_length=255, blank=True, null=True, verbose_name="Parroquia de Quito", choices=PARROQUIAS_QUITO, help_text="Si su provincia de residencia es Pichincha, Elija una parroquia. Caso contrario dejelo en blanco")
    phone_regex = RegexValidator(
        regex=r'^\+?593?\d{9,15}$',
        message="El número de teléfono debe estar en formato internacional. Ejemplo: +593XXXXXXXXX."
    )

    telefono = PhoneNumberField(
        verbose_name="Teléfono",
        validators=[phone_regex],
        default='+593'  # Código de área de Ecuador como valor por defecto
    )
    direccion = models.CharField(max_length=255, blank=True, null=True, verbose_name="Dirección")
    georeferenciacion = models.CharField(max_length=255, blank=True, null=True, verbose_name="Georreferenciación")
    perfil_redes_sociales = models.URLField(blank=True, null=True, verbose_name="Perfil de Redes Sociales", help_text="Pegue aquí la dirección Url de superfil de usuario en redes sociales.")

    class Meta:
        ordering = ['user']
        verbose_name_plural = "Perfiles de Contacto de Usuarios"

    def __str__(self):
        return 'Perfil de Contacto de Usuario {}'.format(self.user.username)





class edit_contact2(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Nombre de Usuario para contacto")
    telefono = models.CharField(max_length=20, verbose_name="Teléfono")
    direccion = models.CharField(max_length=255, blank=True, null=True, verbose_name="Dirección")
    georeferenciacion = models.CharField(max_length=255, blank=True, null=True, verbose_name="Georreferenciación")
    perfil_redes_sociales = models.URLField(blank=True, null=True, verbose_name="Perfil de Redes Sociales")

    class Meta:
        ordering = ['user']
        verbose_name_plural = "Contacto de Usuarios"

    def __str__(self):
        return 'Perfil de contacto de  Usuario {}'.format(self.user.username)

class edit_contact1(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Nombre de Usuario para contacto")
   # date_of_birth = models.DateField(blank=True, null=True, verbose_name="Fecha de Nacimiento")
   # photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, verbose_name="Foto de Perfil")
   
    pais_residencia = CountryField(verbose_name="País de Residencia", default="Ecuador")
    
    PROVINCIAS_CANTONES_CHOICES = (
        ('Azuay', (
                ('Cuenca', 'Cuenca'),
                ('Gualaceo', 'Gualaceo'),
                ('Sígsig', 'Sígsig'),
                ('Chordeleg', 'Chordeleg'),
                ('Sigsig', 'Sigsig'),
                ('Oña', 'Oña'),
                ('Girón', 'Girón'),
                ('Paute', 'Paute'),
                ('Santa Isabel', 'Santa Isabel'),
                ('Nabón', 'Nabón'),
                ('El Pan', 'El Pan'),
                ('Sevilla de Oro', 'Sevilla de Oro'),
                ('Guachapala', 'Guachapala'),
                ('Camilo Ponce Enríquez', 'Camilo Ponce Enríquez'),
                ('Suscal', 'Suscal'),
                ('Pucará', 'Pucará'),
                ('San Fernando', 'San Fernando'),
            )
        ),
        ('Bolívar', (
                ('Guaranda', 'Guaranda'),
                ('Caluma', 'Caluma'),
                ('Chillanes', 'Chillanes'),
                ('Chimbo', 'Chimbo'),
                ('Echeandía', 'Echeandía'),
                ('Las Naves', 'Las Naves'),
            )
        ),
        ('Cañar', (
                ('Azogues', 'Azogues'),
                ('Biblián', 'Biblián'),
                ('Cañar', 'Cañar'),
                ('La Troncal', 'La Troncal'),
                ('Déleg', 'Déleg'),
                ('El Tambo', 'El Tambo'),
                ('Suscal', 'Suscal'),
            )
        ),
        ('Carchi', (
                ('Tulcán', 'Tulcán'),
                ('Bolívar', 'Bolívar'),
                ('Espejo', 'Espejo'),
                ('Mira', 'Mira'),
                ('Montúfar', 'Montúfar'),
                ('San Pedro de Huaca', 'San Pedro de Huaca'),
            )
        ),
        ('Chimborazo', (
                ('Riobamba', 'Riobamba'),
                ('Alausí', 'Alausí'),
                ('Colta', 'Colta'),
                ('Chambo', 'Chambo'),
                ('Chunchi', 'Chunchi'),
                ('Guamote', 'Guamote'),
                ('Guano', 'Guano'),
                ('Pallatanga', 'Pallatanga'),
                ('Penipe', 'Penipe'),
            )
        ),
        ('Cotopaxi', (
                ('Latacunga', 'Latacunga'),
                ('La Maná', 'La Maná'),
                ('Pangua', 'Pangua'),
                ('Pujilí', 'Pujilí'),
                ('Salcedo', 'Salcedo'),
                ('Saquisilí', 'Saquisilí'),
                ('Sigchos', 'Sigchos'),
            )
        ),
        ('El Oro', (
                ('Machala', 'Machala'),
                ('Arenillas', 'Arenillas'),
                ('Atahualpa', 'Atahualpa'),
                ('Balsas', 'Balsas'),
                ('Chilla', 'Chilla'),
                ('El Guabo', 'El Guabo'),
                ('Huaquillas', 'Huaquillas'),
                ('Marcabelí', 'Marcabelí'),
                ('Pasaje', 'Pasaje'),
                ('Piñas', 'Piñas'),
                ('Portovelo', 'Portovelo'),
                ('Santa Rosa', 'Santa Rosa'),
                ('Zaruma', 'Zaruma'),
                ('Las Lajas', 'Las Lajas'),
            )
        ),
        ('Esmeraldas', (
                ('Esmeraldas', 'Esmeraldas'),
                ('Eloy Alfaro', 'Eloy Alfaro'),
                ('Muisne', 'Muisne'),
                ('Quinindé', 'Quinindé'),
                ('San Lorenzo', 'San Lorenzo'),
                ('Atacames', 'Atacames'),
                ('Rioverde', 'Rioverde'),
            )
        ),
        ('Galápagos', (
                ('San Cristóbal', 'San Cristóbal'),
                ('Isabela', 'Isabela'),
                ('Santa Cruz', 'Santa Cruz'),
            )
        ),
        ('Guayas', (
                ('Guayaquil', 'Guayaquil'),
                ('Alfredo Baquerizo Moreno', 'Alfredo Baquerizo Moreno (Juján)'),
                ('Balao', 'Balao'),
                ('Balzar', 'Balzar'),
                ('Colimes', 'Colimes'),
                ('Coronel Marcelino Maridueña', 'Coronel Marcelino Maridueña'),
                ('Daule', 'Daule'),
                ('Durán', 'Durán'),
                ('El Empalme', 'El Empalme'),
                ('El Triunfo', 'El Triunfo'),
                ('Milagro', 'Milagro'),
                ('Naranjal', 'Naranjal'),
                ('Naranjito', 'Naranjito'),
                ('Palestina', 'Palestina'),
                ('Pedro Carbo', 'Pedro Carbo'),
                ('Samborondón', 'Samborondón'),
                ('Santa Lucía', 'Santa Lucía'),
                ('Simón Bolívar', 'Simón Bolívar'),
                ('Yaguachi', 'Yaguachi'),
                ('General Antonio Elizalde (Bucay)', 'General Antonio Elizalde (Bucay)'),
                ('Isidro Ayora', 'Isidro Ayora'),
                ('Lomas de Sargentillo', 'Lomas de Sargentillo'),
                ('Nobol', 'Nobol'),
                ('Santa Elena', 'Santa Elena'),
                ('La Libertad', 'La Libertad'),
                ('Salinas', 'Salinas'),
            )
        ),
        ('Imbabura', (
                ('Ibarra', 'Ibarra'),
                ('Antonio Ante', 'Antonio Ante (Andrade Marin)'),
                ('Cotacachi', 'Cotacachi'),
                ('Otavalo', 'Otavalo'),
                ('Pimampiro', 'Pimampiro'),
                ('San Miguel de Urcuquí', 'San Miguel de Urcuquí'),
            )
        ),
        ('Loja', (
                ('Loja', 'Loja'),
                ('Calvas', 'Calvas'),
                ('Catamayo', 'Catamayo'),
                ('Celica', 'Celica'),
                ('Chaguarpamba', 'Chaguarpamba'),
                ('Espíndola', 'Espíndola'),
                ('Gonzanamá', 'Gonzanamá'),
                ('Macará', 'Macará'),
                ('Paltas', 'Paltas'),
                ('Puyango', 'Puyango'),
                ('Saraguro', 'Saraguro'),
                ('Sozoranga', 'Sozoranga'),
                ('Zapotillo', 'Zapotillo'),
                ('Pindal', 'Pindal'),
                ('Quilanga', 'Quilanga'),
                ('Olmedo', 'Olmedo'),
            )
        ),
        ('Los Ríos', (
                ('Babahoyo', 'Babahoyo'),
                ('Baba', 'Baba'),
                ('Montalvo', 'Montalvo'),
                ('Buena Fe', 'Buena Fe'),
                ('Mocache', 'Mocache'),
                ('Urdaneta', 'Urdaneta'),
                ('Ventanas', 'Ventanas'),
                ('Quevedo', 'Quevedo'),
                ('Quinsaloma', 'Quinsaloma'),
                ('Valencia', 'Valencia'),
                ('Vinces', 'Vinces'),
                ('Palenque', 'Palenque'),
            )
        ),
        ('Manabí', (
                ('Portoviejo', 'Portoviejo'),
                ('Bolívar', 'Bolívar'),
                ('Chone', 'Chone'),
                ('El Carmen', 'El Carmen'),
                ('Flavio Alfaro', 'Flavio Alfaro'),
                ('Jipijapa', 'Jipijapa'),
                ('Junín', 'Junín'),
                ('Manta', 'Manta'),
                ('Montecristi', 'Montecristi'),
                ('Paján', 'Paján'),
                ('Pichincha', 'Pichincha'),
                ('Rocafuerte', 'Rocafuerte'),
                ('Santa Ana', 'Santa Ana'),
                ('Sucre', 'Sucre'),
                ('Tosagua', 'Tosagua'),
                ('24 de Mayo', '24 de Mayo'),
                ('Pedernales', 'Pedernales'),
                ('Olmedo', 'Olmedo'),
                ('Puerto López', 'Puerto López'),
                ('Jama', 'Jama'),
                ('San Vicente', 'San Vicente'),
            )
        ),
        ('Morona Santiago', (
                ('Macas', 'Macas'),
                ('Gualaquiza', 'Gualaquiza'),
                ('Huamboya', 'Huamboya'),
                ('Limón Indanza', 'Limón Indanza'),
                ('Logroño', 'Logroño'),
                ('Morona', 'Morona'),
                ('Pablo Sexto', 'Pablo Sexto'),
                ('Palora', 'Palora'),
                ('San Juan Bosco', 'San Juan Bosco'),
                ('Santiago de Méndez', 'Santiago de Méndez'),
                ('Sucúa', 'Sucúa'),
                ('Taisha', 'Taisha'),
                ('Tiwintza', 'Tiwintza'),
            )
        ),
        ('Napo', (
                ('Tena', 'Tena'),
                ('Archidona', 'Archidona'),
                ('El Chaco', 'El Chaco'),
                ('Quijos', 'Quijos'),
                ('Carlos Julio Arosemena Tola', 'Carlos Julio Arosemena Tola'),
            )
        ),
        ('Orellana', (
                ('Orellana', 'Orellana'),
                ('Aguarico', 'Aguarico'),
                ('La Joya de los Sachas', 'La Joya de los Sachas'),
                ('Loreto', 'Loreto'),
            )
        ),
        ('Pastaza', (
                ('Puyo', 'Puyo'),
                ('Arajuno', 'Arajuno'),
                ('Mera', 'Mera'),
                ('Santa Clara', 'Santa Clara'),
            )
        ),
        ('Pichincha', (
                ('Quito', 'Quito'),
                ('Cayambe', 'Cayambe'),
                ('Mejía', 'Mejía'),
                ('Pedro Moncayo', 'Pedro Moncayo'),
                ('Rumiñahui', 'Rumiñahui'),
                ('San Miguel de los Bancos', 'San Miguel de los Bancos'),
                ('Pedro Vicente Maldonado', 'Pedro Vicente Maldonado'),
                ('Puerto Quito', 'Puerto Quito'),
            )
        ),
        ('Santa Elena', (
                ('Santa Elena', 'Santa Elena'),
                ('La Libertad', 'La Libertad'),
                ('Salinas', 'Salinas'),
            )
        ),
        ('Santo Domingo de los Tsáchilas', (
                ('Santo Domingo', 'Santo Domingo'),
                ('La Concordia', 'La Concordia'),
            )
        ),
        ('Sucumbíos', (
                ('Nueva Loja', 'Nueva Loja'),
                ('Cascales', 'Cascales'),
                ('Cuyabeno', 'Cuyabeno'),
                ('Gonzalo Pizarro', 'Gonzalo Pizarro'),
                ('Putumayo', 'Putumayo'),
                ('Shushufindi', 'Shushufindi'),
                ('Sucumbíos', 'Sucumbíos'),
                ('Lago Agrio', 'Lago Agrio'),
            )
        ),
        ('Tungurahua', (
                ('Ambato', 'Ambato'),
                ('Baños de Agua Santa', 'Baños de Agua Santa'),
                ('Cevallos', 'Cevallos'),
                ('Mocha', 'Mocha'),
                ('Patate', 'Patate'),
                ('Quero', 'Quero'),
                ('San Pedro de Pelileo', 'San Pedro de Pelileo'),
                ('Pelileo', 'Pelileo'),
                ('Pillaro', 'Pillaro'),
                ('Tisaleo', 'Tisaleo'),
            )
        ),
        ('Zamora Chinchipe', (
                ('Zamora', 'Zamora'),
                ('Chinchipe', 'Chinchipe'),
                ('Centinela del Cóndor', 'Centinela del Cóndor'),
                ('Nangaritza', 'Nangaritza'),
                ('Palanda', 'Palanda'),
                ('Paquisha', 'Paquisha'),
                ('Yacuambi', 'Yacuambi'),
                ('Yantzaza', 'Yantzaza'),
                ('El Pangui', 'El Pangui'),
            )
        ),
    )
    
    provincia_cantones_ecuador = models.CharField(max_length=255, blank=True, null=True, verbose_name="Provincia y Cantones", choices=PROVINCIAS_CANTONES_CHOICES, help_text="Si su pais de residencia es Ecuador, Elija una provincia. Caso contrario dejelo en blanco")

    PARROQUIAS_QUITO = (
        ('Conocoto', 'Conocoto'),
        ('Cumbayá', 'Cumbayá'),
        ('Chillogallo', 'Chillogallo'),
        ('Chilibulo', 'Chilibulo'),
        ('Chillos', 'Ch  illos'),
        ('Guamaní', 'Guamaní'),
        ('Calderón', 'Calderón'),
        ('Carapungo', 'Carapungo'),
        ('Pomasqui', 'Pomasqui'),
        ('Nayón', 'Nayón'),
        ('Tumbaco', 'Tumbaco'),
        ('Tababela', 'Tababela'),
        ('Quito', 'Quito'),
    )
    
    parroquia_quito = models.CharField(max_length=255, blank=True, null=True, verbose_name="Parroquia de Quito", choices=PARROQUIAS_QUITO, help_text="Si su provincia de residencia es Pichincha, Elija una parroquia. Caso contrario dejelo en blanco")
    class Meta:
        ordering = ['user']
        verbose_name_plural = "Contacto de Usuarios"

    def __str__(self):
        return 'Perfil de residencia de contacto de  Usuario {}'.format(self.user.username)

    
class Legal(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Nombre de Usuario")
   # date_of_birth = models.DateField(blank=True, null=True, verbose_name="Fecha de Nacimiento")
    lugar_residencia = CountryField(blank=True, null=True, verbose_name="Lugar de Residencia del Representante Legal")
    representante_legal_nombre = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nombre del Representante Legal")
    representante_legal_apellido = models.CharField(max_length=255, blank=True, null=True, verbose_name="Apellido del Representante Legal")
    representante_legal_cedula = models.CharField(max_length=20, blank=True, null=True, verbose_name="Cédula del Representante Legal")
    ruc = models.CharField(max_length=13, blank=True, null=True, verbose_name="RUC")
    phone_regex = RegexValidator(
        regex=r'^\+?593?\d{9,15}$',
        message="El número de teléfono debe estar en formato internacional. Ejemplo: +593XXXXXXXXX."
    )

    telefono_contacto = PhoneNumberField(
        verbose_name="telefono de contacto del representante legal",
        validators=[phone_regex],
        default='+593'  # Código de área de Ecuador como valor por defecto
    )

    direccion_domicilio = models.CharField(max_length=255, blank=True, null=True, verbose_name="Dirección de Domicilio")
    georeferencia = models.CharField(max_length=255, blank=True, null=True, verbose_name="Georreferencia")
    pagina_web = models.URLField(blank=True, null=True, verbose_name="Página Web")
    tipo_personeria = models.CharField(max_length=10, choices=(('Natural', 'Natural'), ('Jurídico', 'Jurídico')), verbose_name="Tipo de Personería")
    categoria_personeria = models.CharField(max_length=100, choices=(
        ('ASOCIACIONES SIN ÁNIMO DE LUCRO', 'Asociaciones sin ánimo de lucro'),
        ('ASOCIACIÓN DE CUENTAS DE PARTICIPACIÓN', 'Asociación de cuentas de participación'),
        ('SOCIEDAD DE ACCIONES SIMPLIFICADAS. S.A.S', 'Sociedad de acciones simplificadas. S.A.S'),
        ('COMPAÑÍA LIMITADA CÍA. LTDA.', 'Compañía limitada Cía. Ltda.'),
        ('EMPRESARIO INDIVIDUAL', 'Empresario individual'),
        ('SOCIEDAD ANÓNIMA S.A.', 'Sociedad anónima S.A.'),
        ('SOCIEDAD COLECTIVA', 'Sociedad colectiva'),
        ('SOCIEDAD COMANDATARIA', 'Sociedad comandataria'),
        ('SOCIEDAD COOPERATIVA', 'Sociedad cooperativa'),
        ('SOCIEDAD LIMITADA S.L.', 'Sociedad limitada S.L.'),
        ('OTRO', 'Otro')
    ), verbose_name="Categoría de Personería Jurídica", blank=True, null= True)
    fines_lucro = models.BooleanField(default=False, verbose_name="¿La personería jurídica tiene fines de lucro?",blank=True, null= True)
    actividad_principal = models.TextField(blank=True, null=True, verbose_name="Actividad Principal a la que se dedica la empresa")

    def __str__(self):
        return 'Informaciíon de Personería jurídica {}'.format(self.user.username)
    
class Activity(models.Model):
    DISCIPLINAS_ARTISTICAS_CHOICES = [
        ('ARTES ESCÉNICAS', 'Artes Escénicas'),
        ('ARTES VISUALES O PLÁSTICAS', 'Artes Visuales o Plásticas'),
        ('ARTES MUSICALES', 'Artes Musicales'),
        ('ARTES AUDIOVISUALES', 'Artes Audiovisuales'),
        ('ARTES LITERARIAS', 'Artes Literarias'),
        ('ARTESANÍAS', 'Artesanías'),
        ('FORMACIÓN ARTÍSTICA', 'Formación Artística'),
        ('MEMORIA SOCIAL Y PATRIMONIO INTANGIBLE', 'Memoria Social y Patrimonio Intangible'),
        ('OTROS', 'Otros')
    ]

    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Nombre de Usuario")
   #date_of_birth = models.DateField(blank=True, null=True, verbose_name="Fecha de Nacimiento")
   # photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, verbose_name="Foto de Perfil")
    disciplina_artistica = models.CharField(max_length=100, choices=DISCIPLINAS_ARTISTICAS_CHOICES, verbose_name="Disciplina/s Artística/s en la que enmarca sus actividades")
    experiencia_ambito_cultural = models.TextField(blank=True, null=True, verbose_name="Experiencia en el ámbito cultural")
    portafolio = models.URLField(blank=True, null=True, verbose_name="Portafolio")
    registro_ruac = models.BooleanField(default=False, verbose_name="¿Es parte del Registro Único de Artistas y Gestores Culturales - RUAC?")
    pertenece_agremiacion_colectivo = models.BooleanField(default=False, verbose_name="¿Pertenece a alguna Agremiación / Colectivo?")
    nombre_agremiacion = models.CharField(max_length=255, blank=True, null=True, verbose_name="Nombre de la Agremiación", help_text="Si pertence a una agremiación artistica, escriba el nombre de la misma. Caso contrario, deje el campo en blanco. ")

    def __str__(self):
        return 'Perfil de Actividad Artistica de Usuario {}'.format(self.user.username)
    
class DeclaracionVeracidad(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, verbose_name="Nombre de Usuario")
    acepta_terminos_condiciones = models.BooleanField(default=False, verbose_name="Acepta los Términos y Condiciones de Uso")

    def __str__(self):
        return f"Declaración de veracidad de usuario: {self.user.username}"

    def save(self, *args, **kwargs):
        # Guardar en caché el valor de acepta_terminos_condiciones
        cache_key = f"user_{self.user.id}_acepta_terminos_condiciones"
        cache.set(cache_key, self.acepta_terminos_condiciones)
        super().save(*args, **kwargs)

    @property
    def get_acepta_terminos_condiciones(self):
        # Obtener el valor de acepta_terminos_condiciones desde caché
        cache_key = f"user_{self.user.id}_acepta_terminos_condiciones"
        return cache.get(cache_key, self.acepta_terminos_condiciones)
    
class confirmacion(models.Model):
    mensaje_de_despedida = RichTextField(default=False, verbose_name="Términos y Condiciones de Uso")


    

class Dashboard(models.Model):
    titulo = models.CharField(max_length=100)
    informacion_basica = RichTextField()
    bloque_1 = RichTextField(blank=True, null=True)
    bloque_2 = RichTextField(blank=True, null=True)
    bloque_3 = RichTextField(blank=True, null=True)
    bloque_4 = RichTextField(blank=True, null=True)
    bloque_5 = RichTextField(blank=True, null=True)
    link_soporte_tecnico = models.URLField()

    def __str__(self):
        return self.titulo


class PrivacyPolicy(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class TermsOfUse(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title

class ActivityPrivacyPolicy(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
    

class ActivityTermsOfUse(models.Model):
    title = models.CharField(max_length=100)
    content = models.TextField()
    last_updated = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title