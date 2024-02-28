from django.db import models
from django.conf import settings
from datetime import datetime
from phonenumber_field.modelfields import PhoneNumberField
from ckeditor.fields import RichTextField
from django.urls import reverse

class Profile(models.Model):
    ETNICA = [
        ('Indígena','Indígena'),
        ('Afroecuatoriano','Afroecuatoriano'),
        ('Montubio','Montubio'),
        ('Mestizo/a','Mestizo/a'),
        ('Blanco/a','Blanco/a'),
        ('Otro/a','Otro/a'),
    ]

    GENERO = [
        ('Masculino','Masculino'),
        ('Femenino','Femenino'),
        ('No binario','Montubio'),
        ('Género fluido','Género fluido'),
        ('Bigénero','Bigénero'),
        ('Transexual','Transexual'),
        ('Andrógino','Andrógino'),
    ]


    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE)
    date_of_birth = models.DateField(blank=True, null=True,verbose_name="Fecha de nacimiento")
    photo = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True)
    numero_cedula = models.CharField(max_length=10,  verbose_name="Número de cedula",null=True)
    dactilar =  models.CharField(max_length=9,  verbose_name="Código Dactilar",null=True)
    nacionalidad = models.CharField(max_length=125,  verbose_name="Nacionalidad",null=True)
    fecha_nacimiento = models.DateField(null=True)
    edad = models.IntegerField(blank=True, null=True)
    seudonimo = models.CharField(max_length=125,  verbose_name="Seudónimo",null=True)
    autoidenty_etnica =  models.CharField(choices=ETNICA, max_length=200,null=True, verbose_name="Autoidentificación Etnica")
    genero = models.CharField(choices=GENERO, max_length=200,null=True,verbose_name="Autoidentificación Género")

    def calcular_edad(self):
        if self.fecha_nacimiento:
            today = datetime.today()
            born = self.fecha_nacimiento
            self.edad = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        else:
            self.edad = None

    def save(self, *args, **kwargs):
        self.calcular_edad()
        super(Profile, self).save(*args, **kwargs)

    def __str__(self):
        return 'Perfil de usuario {}'.format(self.user.username)
    class Meta:
        verbose_name = 'Perfil de Postulantes'
        verbose_name_plural = 'Perfiles de postulantes'
    
class contacto(models.Model):
    PROVINCIA = [
        ('Azuay','Azuay'),
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

    CANTONES_BOLIVAR = (
        ('Guaranda', 'Guaranda'),
        ('Chillanes', 'Chillanes'),
        ('Chimbo', 'Chimbo'),
        ('Echeandía', 'Echeandía'),
        ('San Miguel', 'San Miguel'),
        ('Caluma', 'Caluma'),
    )

    CANTONES_CAÑAR = (
        ('Azogues', 'Azogues'),
        ('Biblián', 'Biblián'),
        ('Cañar', 'Cañar'),
        ('La Troncal', 'La Troncal'),
        ('Déleg', 'Déleg'),
        ('El Tambo', 'El Tambo'),
        ('Suscal', 'Suscal'),
    )

    CANTONES_CARCHI = (
        ('Tulcán', 'Tulcán'),
        ('Bolívar', 'Bolívar'),
        ('Espejo', 'Espejo'),
        ('Mira', 'Mira'),
        ('Montúfar', 'Montúfar'),
        ('San Pedro de Huaca', 'San Pedro de Huaca'),
    )

    CANTONES_CHIMBORAZO = (
        ('Riobamba', 'Riobamba'),
        ('Alausí', 'Alausí'),
        ('Chambo', 'Chambo'),
        ('Chunchi', 'Chunchi'),
        ('Colta', 'Colta'),
        ('Cumandá', 'Cumandá'),
        ('Guamote', 'Guamote'),
        ('Guano', 'Guano'),
        ('Pallatanga', 'Pallatanga'),
        ('Penipe', 'Penipe'),
    )

    CANTONES_COTOPAXI = (
        ('Latacunga', 'Latacunga'),
        ('La Maná', 'La Maná'),
        ('Pangua', 'Pangua'),
        ('Pujilí', 'Pujilí'),
        ('Salcedo', 'Salcedo'),
        ('Saquisilí', 'Saquisilí'),
        ('Sigchos', 'Sigchos'),
    )

    CANTONES_ESMERALDAS = (
        ('Esmeraldas', 'Esmeraldas'),
        ('Atacames', 'Atacames'),
        ('Eloy Alfaro', 'Eloy Alfaro'),
        ('Muisne', 'Muisne'),
        ('Quinindé', 'Quinindé'),
        ('San Lorenzo', 'San Lorenzo'),
    )

    CANTONES_GALAPAGOS = (
        ('San Cristóbal', 'San Cristóbal'),
        ('Santa Cruz', 'Santa Cruz'),
        ('Isabela', 'Isabela'),
    )

    CANTONES_IMBABURA = (
        ('Ibarra', 'Ibarra'),
        ('Antonio Ante', 'Antonio Ante'),
        ('Cotacachi', 'Cotacachi'),
        ('Otavalo', 'Otavalo'),
        ('Pimampiro', 'Pimampiro'),
        ('San Miguel de Urcuquí', 'San Miguel de Urcuquí'),
    )

    CANTONES_LOJA = (
        ('Loja', 'Loja'),
        ('Calvas', 'Calvas'),
        ('Catamayo', 'Catamayo'),
        ('Celica', 'Celica'),
        ('Chaguarpamba', 'Chaguarpamba'),
        ('Espíndola', 'Espíndola'),
        ('Gonzanamá', 'Gonzanamá'),
        ('Macará', 'Macará'),
        ('Paltas', 'Paltas'),
        ('Pindal', 'Pindal'),
        ('Puyango', 'Puyango'),
        ('Quilanga', 'Quilanga'),
        ('Saraguro', 'Saraguro'),
        ('Sozoranga', 'Sozoranga'),
        ('Zapotillo', 'Zapotillo'),
    )

    CANTONES_LOS_RIOS = (
        ('Babahoyo', 'Babahoyo'),
        ('Baba', 'Baba'),
        ('Montalvo', 'Montalvo'),
        ('Pueblo Viejo', 'Pueblo Viejo'),
        ('Quevedo', 'Quevedo'),
        ('Urdaneta', 'Urdaneta'),
        ('Ventanas', 'Ventanas'),
        ('Vinces', 'Vinces'),
    )

    CANTONES_MANABI = (
        ('Portoviejo', 'Portoviejo'),
        ('Chone', 'Chone'),
        ('El Carmen', 'El Carmen'),
        ('Jipijapa', 'Jipijapa'),
        ('Manta', 'Manta'),
        ('Montecristi', 'Montecristi'),
        ('Santa Ana', 'Santa Ana'),
        ('Sucre', 'Sucre'),
        ('Tosagua', 'Tosagua'),
        ('24 de Mayo', '24 de Mayo'),
        ('Bolívar', 'Bolívar'),
        ('Junín', 'Junín'),
        ('Paján', 'Paján'),
        ('Jaramijó', 'Jaramijó'),
        ('Olmedo', 'Olmedo'),
        ('Pedernales', 'Pedernales'),
        ('Puerto López', 'Puerto López'),
        ('San Vicente', 'San Vicente'),
    )

    CANTONES_MORONA_SANTIAGO = (
        ('Morona', 'Morona'),
        ('Gualaquiza', 'Gualaquiza'),
        ('Limoncocha', 'Limoncocha'),
        ('Palora', 'Palora'),
        ('Santiago', 'Santiago'),
        ('Sucúa', 'Sucúa'),
        ('Huamboya', 'Huamboya'),
    )

    CANTONES_NAPO = (
        ('Tena', 'Tena'),
        ('Archidona', 'Archidona'),
        ('El Chaco', 'El Chaco'),
        ('Quijos', 'Quijos'),
    )

    CANTONES_ORELLANA = (
        ('Orellana', 'Orellana'),
        ('Aguarico', 'Aguarico'),
        ('La Joya de los Sachas', 'La Joya de los Sachas'),
    )

    CANTONES_PASTAZA = (
        ('Pastaza', 'Pastaza'),
        ('Mera', 'Mera'),
        ('Santa Clara', 'Santa Clara'),
        ('Arajuno', 'Arajuno'),
    )

    CANTONES_PICHINCHA = (
        ('Quito', 'Quito'),
        ('Cayambe', 'Cayambe'),
        ('Mejía', 'Mejía'),
        ('Pedro Moncayo', 'Pedro Moncayo'),
        ('Pedro Vicente Maldonado', 'Pedro Vicente Maldonado'),
        ('Puerto Quito', 'Puerto Quito'),
        ('Rumiñahui', 'Rumiñahui'),
        ('San Miguel de Los Bancos', 'San Miguel de Los Bancos'),
    )

    CANTONES_SANTA_ELENA = (
        ('Santa Elena', 'Santa Elena'),
        ('La Libertad', 'La Libertad'),
        ('Salinas', 'Salinas'),
    )

    CANTONES_SANTO_DOMINGO = (
        ('Santo Domingo', 'Santo Domingo'),
        ('La Concordia', 'La Concordia'),
    )

    CANTONES_SUCUMBIOS = (
        ('Lago Agrio', 'Lago Agrio'),
        ('Gonzalo Pizarro', 'Gonzalo Pizarro'),
        ('Putumayo', 'Putumayo'),
        ('Shushufindi', 'Shushufindi'),
    )

    CANTONES_TUNGURAHUA = (
        ('Ambato', 'Ambato'),
        ('Baños de Agua Santa', 'Baños de Agua Santa'),
        ('Cevallos', 'Cevallos'),
        ('Mocha', 'Mocha'),
        ('Patate', 'Patate'),
        ('Quero', 'Quero'),
        ('Pelileo', 'Pelileo'),
        ('Pillaro', 'Pillaro'),
        ('Tisaleo', 'Tisaleo'),
    )

    CANTONES_ZAMORA_CHINCHIPE = (
        ('Zamora', 'Zamora'),
        ('Chinchipe', 'Chinchipe'),
        ('Nangaritza', 'Nangaritza'),
        ('Yacuambi', 'Yacuambi'),
        ('Yantzaza', 'Yantzaza'),
        ('El Pangui', 'El Pangui'),
        ('Centinela del Cóndor', 'Centinela del Cóndor'),
        ('Palanda', 'Palanda'),
        ('Paquisha', 'Paquisha'),
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

    PARROQUIAS_BOLIVAR = (
        ('Guaranda', (
            ('Guaranda', 'Guaranda'),
            ('Facundo Vela', 'Facundo Vela'),
            ('Julio E. Moreno', 'Julio E. Moreno'),
            ('Salinas', 'Salinas'),
        )),
        ('Caluma', (
            ('Caluma', 'Caluma'),
            ('La Victoria', 'La Victoria'),
            ('San Luis de Pambil', 'San Luis de Pambil'),
        )),
        ('Chillanes', (
            ('Chillanes', 'Chillanes'),
            ('San José del Tambo', 'San José del Tambo'),
        )),
        # Agrega las demás parroquias según sea necesario
    )

    PARROQUIAS_CAÑAR = (
        ('Azogues', 'Azogues'),
        ('Biblián', 'Biblián'),
        ('Cañar', 'Cañar'),
        ('Déleg', 'Déleg'),
        ('El Tambo', 'El Tambo'),
        ('La Troncal', 'La Troncal'),
        ('Suscal', 'Suscal'),
    )

    CANTONES_CARCHI = (
        ('Tulcán', (
            ('González Suárez', 'González Suárez'),
            ('Tufiño', 'Tufiño'),
            # Otras parroquias del cantón Tulcán
        )),
        ('Bolívar', (
            ('Bolívar', 'Bolívar'),
            ('García Moreno', 'García Moreno'),
            # Otras parroquias del cantón Bolívar
        )),
        ('Espejo', (
            ('El Ángel', 'El Ángel'),
            ('El Goaltal', 'El Goaltal'),
            # Otras parroquias del cantón Espejo
        )),
        # Otros cantones de la provincia de Carchi
    )

    PARROQUIAS_CHIMBORAZO = (
        ('Riobamba', (
                ('Riobamba', 'Riobamba'),
                ('Lizarzaburu', 'Lizarzaburu'),
                ('Licán', 'Licán'),
                # Otras parroquias de Riobamba
            )
        ),
        ('Alausí', (
                ('Alausí', 'Alausí'),
                ('Achupallas', 'Achupallas'),
                # Otras parroquias de Alausí
            )
        ),
        # Otros cantones de Chimborazo
    )

    PARROQUIAS_COTOPAXI = (
        ('Latacunga', (
            ('La Matriz', 'La Matriz'),
            ('Eloy Alfaro (San Felipe)', 'Eloy Alfaro (San Felipe)'),
            ('Ignacio Flores (Parque La Libertad)', 'Ignacio Flores (Parque La Libertad)'),
            # Añade más parroquias de Latacunga si es necesario
        )),
        ('Salcedo', (
            ('San Miguel', 'San Miguel'),
            ('Antonio José Holguín (Santa Lucía)', 'Antonio José Holguín (Santa Lucía)'),
            # Añade más parroquias de Salcedo si es necesario
        )),
        ('Pujilí', (
            ('San Francisco de Pujilí', 'San Francisco de Pujilí'),
            ('Alaques (Alaquez)', 'Alaques (Alaquez)'),
            # Añade más parroquias de Pujilí si es necesario
        )),
        # Añade más cantones de Cotopaxi con sus respectivas parroquias si es necesario
    )

    PARROQUIAS_ESMERALDAS = (
        ('Atacames', 'Atacames'),
        ('La Unión', 'La Unión'),
        ('Limones', 'Limones'),
        ('Río Verde', 'Río Verde'),
        ('Tonsupa', 'Tonsupa'),
        # Agrega más parroquias según sea necesario
    )

    PARROQUIAS_GALAPAGOS = (
        ('Puerto Ayora', 'Puerto Ayora'),
        ('Puerto Baquerizo Moreno', 'Puerto Baquerizo Moreno'),
        # Agrega aquí más parroquias según sea necesario
    )

    PARROQUIAS_IMBABURA = (
        ('Ibarra', (
                ('Caranqui', 'Caranqui'),
                ('La Dolorosa del Priorato', 'La Dolorosa del Priorato'),
                ('San Antonio de Ibarra', 'San Antonio de Ibarra'),
                ('San Francisco de Ibarra', 'San Francisco de Ibarra'),
                ('Sagrario', 'Sagrario'),
            )
        ),
        ('Otavalo', (
                ('Dr. Miguel Egas Cabezas', 'Dr. Miguel Egas Cabezas'),
                ('Cotacachi', 'Cotacachi'),
                ('Otavalo', 'Otavalo'),
                ('San José de Quichinche', 'San José de Quichinche'),
                ('San Juan de Ilumán', 'San Juan de Ilumán'),
                ('San Pablo', 'San Pablo'),
            )
        ),
        # Otras parroquias de Imbabura aquí
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    provincia =  models.CharField(choices=PROVINCIA, max_length=200,null=True)
    canton1 = models.CharField(choices=CANTONES_AZUAY, max_length=200,null=True)
    canton2 = models.CharField(choices=CANTONES_BOLIVAR, max_length=200,null=True)
    canton3 = models.CharField(choices=CANTONES_CAÑAR, max_length=200,null=True)
    canton4 = models.CharField(choices=CANTONES_CARCHI, max_length=200,null=True)
    canton5 = models.CharField(choices=CANTONES_CHIMBORAZO, max_length=200,null=True)
    canton6 = models.CharField(choices=CANTONES_COTOPAXI, max_length=200,null=True)
    canton7 = models.CharField(choices=CANTONES_ESMERALDAS, max_length=200,null=True)
    canton8 = models.CharField(choices=CANTONES_GALAPAGOS, max_length=200,null=True)
    canton9 = models.CharField(choices=CANTONES_IMBABURA, max_length=200,null=True)
    canton10 = models.CharField(choices=CANTONES_LOJA, max_length=200,null=True)
    canton11 = models.CharField(choices=CANTONES_LOS_RIOS, max_length=200,null=True)
    canton12 = models.CharField(choices=CANTONES_MANABI, max_length=200,null=True)
    canton13 = models.CharField(choices=CANTONES_MORONA_SANTIAGO, max_length=200,null=True)
    canton14 = models.CharField(choices=CANTONES_NAPO, max_length=200,null=True)
    canton15 = models.CharField(choices=CANTONES_ORELLANA, max_length=200,null=True)
    canton16 = models.CharField(choices=CANTONES_PASTAZA, max_length=200,null=True)
    canton17 = models.CharField(choices=CANTONES_PICHINCHA, max_length=200,null=True)
    canton18 = models.CharField(choices=CANTONES_SANTA_ELENA, max_length=200,null=True)
    canton19 = models.CharField(choices=CANTONES_SANTO_DOMINGO, max_length=200,null=True)
    canton20 = models.CharField(choices=CANTONES_SUCUMBIOS, max_length=200,null=True)
    canton21 = models.CharField(choices=CANTONES_TUNGURAHUA, max_length=200,null=True)
    canton22 = models.CharField(choices=CANTONES_ZAMORA_CHINCHIPE, max_length=200,null=True)
    parroquia1 = models.CharField(choices=PARROQUIAS_AZUAY, max_length=200,null=True)
    parroquia2 = models.CharField(choices=PARROQUIAS_BOLIVAR, max_length=200,null=True)
    parroquia3 = models.CharField(choices=PARROQUIAS_CAÑAR, max_length=200,null=True)
    parroquia4 = models.CharField(choices=CANTONES_CARCHI, max_length=200,null=True)
    parroquia5 = models.CharField(choices=PARROQUIAS_CHIMBORAZO, max_length=200,null=True)
    parroquia6 = models.CharField(choices=PARROQUIAS_COTOPAXI, max_length=200,null=True)
    parroquia7 = models.CharField(choices=PARROQUIAS_ESMERALDAS, max_length=200,null=True)
    parroquia8 = models.CharField(choices=PARROQUIAS_GALAPAGOS, max_length=200,null=True)
    parroquia9 = models.CharField(choices=PARROQUIAS_IMBABURA, max_length=200,null=True)
    direccion = models.CharField( max_length=200,null=True)
    gero_ref = models.CharField( max_length=200,null=True)
    telefono = PhoneNumberField(null=True)

    def __str__(self):
        return 'Contacto de usuario {}'.format(self.user.get_full_name)
    class Meta:
        verbose_name = 'Información de contacto de Postulante'
        verbose_name_plural = 'Información de contactos de Postulantes'



class legal(models.Model):

    LEGAL = [('Natural','Natural'),('Jurídico','Jurídico')]
    LEGAL2 = [('ASOCIACIONES SIN ÁNIMO DE LUCRO','ASOCIACIONES SIN ÁNIMO DE LUCRO'),
              ('ASOCIACIÓN DE CUENTAS DE PARTICIPACIÓN','ASOCIACIÓN DE CUENTAS DE PARTICIPACIÓN'),
              ('COMPAÑÍA LIMITADA CÍA. LTDA.','COMPAÑÍA LIMITADA CÍA. LTDA.'),
              ('EMPRESARIO INDIVIDUAL','EMPRESARIO INDIVIDUAL'),
              ('SOCIEDAD ANÓNIMA S.A.','SOCIEDAD ANÓNIMA S.A.'),
              ('SOCIEDAD DE ACCIONES SIMPLIFICADA S.A.S','SOCIEDAD DE ACCIONES SIMPLIFICADA S.A.S'),
              ('SOCIEDAD COLECTIVA','SOCIEDAD COLECTIVA.'),   
              ('SOCIEDAD COMANDATARIA','SOCIEDAD COMANDATARIA'), 
              ('SOCIEDAD COOPERATIVA','SOCIEDAD COOPERATIVA'),  
              ('SOCIEDAD LIMITADA S.L.','SOCIEDAD LIMITADA S.L.'),      ]
    ETNICA = [
        ('Indígena','Indígena'),
        ('Afroecuatoriano','Afroecuatoriano'),
        ('Montubio','Montubio'),
        ('Mestizo/a','Mestizo/a'),
        ('Blanco/a','Blanco/a'),
        ('Otro/a','Otro/a'),
    ]

    GENERO = [
        ('Masculino','Masculino'),
        ('Femenino','Femenino'),
        ('No binario','Montubio'),
        ('Género fluido','Género fluido'),
        ('Bigénero','Bigénero'),
        ('Transexual','Transexual'),
        ('Andrógino','Andrógino'),
    ]

    opciones = [
        ('Si','Si'),
        ('No','No'),
    ]

    
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    ruc = models.IntegerField(blank=True, null=True, verbose_name = "¿Usted dispone de R.U.C?")
    natu_juri =  models.CharField(choices=LEGAL, max_length=200,null=True, verbose_name = "¿En que estado legal desea realizar su registro?")
    tipo_jury =  models.CharField(choices=LEGAL2, max_length=200,null=True, verbose_name = "Tipo de personería jurídica")
    lucro_jury =   models.CharField( choices=opciones, max_length=200,null=True, verbose_name = "¿ La personería jurídica tiene fines de lucro ?a")
    activity_jury =  models.CharField(max_length=200,null=True, verbose_name = "ACTIVIDAD PRINCIPAL A LA QUE SE DEDICA LA EMPRESA")
    numero_cedula = models.CharField(max_length=10,  verbose_name="Número de cedula del representante legal",null=True)
    dactilar =  models.CharField(max_length=9,  verbose_name="Código Dactilar del representante legal",null=True)
    nacionalidad = models.CharField(max_length=125,  verbose_name="Nacionalidad del representante legal",null=True)
    fecha_nacimiento = models.DateField(null=True, verbose_name="Fecha de nacimiento del representante legal")
    edad = models.IntegerField(blank=True, null=True,verbose_name="Edad del representante legal")
    autoidenty_etnica =  models.CharField(choices=ETNICA, max_length=200,null=True, verbose_name="Autoidentificación Etnica del representante legal")
    genero = models.CharField(choices=GENERO, max_length=200,null=True,verbose_name="Autoidentificación Género del representante legal")

    def calcular_edad(self):
        if self.fecha_nacimiento:
            today = datetime.today()
            born = self.fecha_nacimiento
            self.edad = today.year - born.year - ((today.month, today.day) < (born.month, born.day))
        else:
            self.edad = None


    def __str__(self):
        return 'Informaciín legal de usuario {}'.format(self.user.get_full_name)
    class Meta:
        verbose_name = 'Estatus legal de Postulante'
        verbose_name_plural = 'Estatus legal de Postulantes'


class contacto_legal(models.Model):

    PROVINCIA = [
        ('Azuay','Azuay'),
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

    CANTONES_BOLIVAR = (
        ('Guaranda', 'Guaranda'),
        ('Chillanes', 'Chillanes'),
        ('Chimbo', 'Chimbo'),
        ('Echeandía', 'Echeandía'),
        ('San Miguel', 'San Miguel'),
        ('Caluma', 'Caluma'),
    )

    CANTONES_CAÑAR = (
        ('Azogues', 'Azogues'),
        ('Biblián', 'Biblián'),
        ('Cañar', 'Cañar'),
        ('La Troncal', 'La Troncal'),
        ('Déleg', 'Déleg'),
        ('El Tambo', 'El Tambo'),
        ('Suscal', 'Suscal'),
    )

    CANTONES_CARCHI = (
        ('Tulcán', 'Tulcán'),
        ('Bolívar', 'Bolívar'),
        ('Espejo', 'Espejo'),
        ('Mira', 'Mira'),
        ('Montúfar', 'Montúfar'),
        ('San Pedro de Huaca', 'San Pedro de Huaca'),
    )

    CANTONES_CHIMBORAZO = (
        ('Riobamba', 'Riobamba'),
        ('Alausí', 'Alausí'),
        ('Chambo', 'Chambo'),
        ('Chunchi', 'Chunchi'),
        ('Colta', 'Colta'),
        ('Cumandá', 'Cumandá'),
        ('Guamote', 'Guamote'),
        ('Guano', 'Guano'),
        ('Pallatanga', 'Pallatanga'),
        ('Penipe', 'Penipe'),
    )

    CANTONES_COTOPAXI = (
        ('Latacunga', 'Latacunga'),
        ('La Maná', 'La Maná'),
        ('Pangua', 'Pangua'),
        ('Pujilí', 'Pujilí'),
        ('Salcedo', 'Salcedo'),
        ('Saquisilí', 'Saquisilí'),
        ('Sigchos', 'Sigchos'),
    )

    CANTONES_ESMERALDAS = (
        ('Esmeraldas', 'Esmeraldas'),
        ('Atacames', 'Atacames'),
        ('Eloy Alfaro', 'Eloy Alfaro'),
        ('Muisne', 'Muisne'),
        ('Quinindé', 'Quinindé'),
        ('San Lorenzo', 'San Lorenzo'),
    )

    CANTONES_GALAPAGOS = (
        ('San Cristóbal', 'San Cristóbal'),
        ('Santa Cruz', 'Santa Cruz'),
        ('Isabela', 'Isabela'),
    )

    CANTONES_IMBABURA = (
        ('Ibarra', 'Ibarra'),
        ('Antonio Ante', 'Antonio Ante'),
        ('Cotacachi', 'Cotacachi'),
        ('Otavalo', 'Otavalo'),
        ('Pimampiro', 'Pimampiro'),
        ('San Miguel de Urcuquí', 'San Miguel de Urcuquí'),
    )

    CANTONES_LOJA = (
        ('Loja', 'Loja'),
        ('Calvas', 'Calvas'),
        ('Catamayo', 'Catamayo'),
        ('Celica', 'Celica'),
        ('Chaguarpamba', 'Chaguarpamba'),
        ('Espíndola', 'Espíndola'),
        ('Gonzanamá', 'Gonzanamá'),
        ('Macará', 'Macará'),
        ('Paltas', 'Paltas'),
        ('Pindal', 'Pindal'),
        ('Puyango', 'Puyango'),
        ('Quilanga', 'Quilanga'),
        ('Saraguro', 'Saraguro'),
        ('Sozoranga', 'Sozoranga'),
        ('Zapotillo', 'Zapotillo'),
    )

    CANTONES_LOS_RIOS = (
        ('Babahoyo', 'Babahoyo'),
        ('Baba', 'Baba'),
        ('Montalvo', 'Montalvo'),
        ('Pueblo Viejo', 'Pueblo Viejo'),
        ('Quevedo', 'Quevedo'),
        ('Urdaneta', 'Urdaneta'),
        ('Ventanas', 'Ventanas'),
        ('Vinces', 'Vinces'),
    )

    CANTONES_MANABI = (
        ('Portoviejo', 'Portoviejo'),
        ('Chone', 'Chone'),
        ('El Carmen', 'El Carmen'),
        ('Jipijapa', 'Jipijapa'),
        ('Manta', 'Manta'),
        ('Montecristi', 'Montecristi'),
        ('Santa Ana', 'Santa Ana'),
        ('Sucre', 'Sucre'),
        ('Tosagua', 'Tosagua'),
        ('24 de Mayo', '24 de Mayo'),
        ('Bolívar', 'Bolívar'),
        ('Junín', 'Junín'),
        ('Paján', 'Paján'),
        ('Jaramijó', 'Jaramijó'),
        ('Olmedo', 'Olmedo'),
        ('Pedernales', 'Pedernales'),
        ('Puerto López', 'Puerto López'),
        ('San Vicente', 'San Vicente'),
    )

    CANTONES_MORONA_SANTIAGO = (
        ('Morona', 'Morona'),
        ('Gualaquiza', 'Gualaquiza'),
        ('Limoncocha', 'Limoncocha'),
        ('Palora', 'Palora'),
        ('Santiago', 'Santiago'),
        ('Sucúa', 'Sucúa'),
        ('Huamboya', 'Huamboya'),
    )

    CANTONES_NAPO = (
        ('Tena', 'Tena'),
        ('Archidona', 'Archidona'),
        ('El Chaco', 'El Chaco'),
        ('Quijos', 'Quijos'),
    )

    CANTONES_ORELLANA = (
        ('Orellana', 'Orellana'),
        ('Aguarico', 'Aguarico'),
        ('La Joya de los Sachas', 'La Joya de los Sachas'),
    )

    CANTONES_PASTAZA = (
        ('Pastaza', 'Pastaza'),
        ('Mera', 'Mera'),
        ('Santa Clara', 'Santa Clara'),
        ('Arajuno', 'Arajuno'),
    )

    CANTONES_PICHINCHA = (
        ('Quito', 'Quito'),
        ('Cayambe', 'Cayambe'),
        ('Mejía', 'Mejía'),
        ('Pedro Moncayo', 'Pedro Moncayo'),
        ('Pedro Vicente Maldonado', 'Pedro Vicente Maldonado'),
        ('Puerto Quito', 'Puerto Quito'),
        ('Rumiñahui', 'Rumiñahui'),
        ('San Miguel de Los Bancos', 'San Miguel de Los Bancos'),
    )

    CANTONES_SANTA_ELENA = (
        ('Santa Elena', 'Santa Elena'),
        ('La Libertad', 'La Libertad'),
        ('Salinas', 'Salinas'),
    )

    CANTONES_SANTO_DOMINGO = (
        ('Santo Domingo', 'Santo Domingo'),
        ('La Concordia', 'La Concordia'),
    )

    CANTONES_SUCUMBIOS = (
        ('Lago Agrio', 'Lago Agrio'),
        ('Gonzalo Pizarro', 'Gonzalo Pizarro'),
        ('Putumayo', 'Putumayo'),
        ('Shushufindi', 'Shushufindi'),
    )

    CANTONES_TUNGURAHUA = (
        ('Ambato', 'Ambato'),
        ('Baños de Agua Santa', 'Baños de Agua Santa'),
        ('Cevallos', 'Cevallos'),
        ('Mocha', 'Mocha'),
        ('Patate', 'Patate'),
        ('Quero', 'Quero'),
        ('Pelileo', 'Pelileo'),
        ('Pillaro', 'Pillaro'),
        ('Tisaleo', 'Tisaleo'),
    )

    CANTONES_ZAMORA_CHINCHIPE = (
        ('Zamora', 'Zamora'),
        ('Chinchipe', 'Chinchipe'),
        ('Nangaritza', 'Nangaritza'),
        ('Yacuambi', 'Yacuambi'),
        ('Yantzaza', 'Yantzaza'),
        ('El Pangui', 'El Pangui'),
        ('Centinela del Cóndor', 'Centinela del Cóndor'),
        ('Palanda', 'Palanda'),
        ('Paquisha', 'Paquisha'),
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

    PARROQUIAS_BOLIVAR = (
        ('Guaranda', (
            ('Guaranda', 'Guaranda'),
            ('Facundo Vela', 'Facundo Vela'),
            ('Julio E. Moreno', 'Julio E. Moreno'),
            ('Salinas', 'Salinas'),
        )),
        ('Caluma', (
            ('Caluma', 'Caluma'),
            ('La Victoria', 'La Victoria'),
            ('San Luis de Pambil', 'San Luis de Pambil'),
        )),
        ('Chillanes', (
            ('Chillanes', 'Chillanes'),
            ('San José del Tambo', 'San José del Tambo'),
        )),
        # Agrega las demás parroquias según sea necesario
    )

    PARROQUIAS_CAÑAR = (
        ('Azogues', 'Azogues'),
        ('Biblián', 'Biblián'),
        ('Cañar', 'Cañar'),
        ('Déleg', 'Déleg'),
        ('El Tambo', 'El Tambo'),
        ('La Troncal', 'La Troncal'),
        ('Suscal', 'Suscal'),
    )

    CANTONES_CARCHI = (
        ('Tulcán', (
            ('González Suárez', 'González Suárez'),
            ('Tufiño', 'Tufiño'),
            # Otras parroquias del cantón Tulcán
        )),
        ('Bolívar', (
            ('Bolívar', 'Bolívar'),
            ('García Moreno', 'García Moreno'),
            # Otras parroquias del cantón Bolívar
        )),
        ('Espejo', (
            ('El Ángel', 'El Ángel'),
            ('El Goaltal', 'El Goaltal'),
            # Otras parroquias del cantón Espejo
        )),
        # Otros cantones de la provincia de Carchi
    )

    PARROQUIAS_CHIMBORAZO = (
        ('Riobamba', (
                ('Riobamba', 'Riobamba'),
                ('Lizarzaburu', 'Lizarzaburu'),
                ('Licán', 'Licán'),
                # Otras parroquias de Riobamba
            )
        ),
        ('Alausí', (
                ('Alausí', 'Alausí'),
                ('Achupallas', 'Achupallas'),
                # Otras parroquias de Alausí
            )
        ),
        # Otros cantones de Chimborazo
    )

    PARROQUIAS_COTOPAXI = (
        ('Latacunga', (
            ('La Matriz', 'La Matriz'),
            ('Eloy Alfaro (San Felipe)', 'Eloy Alfaro (San Felipe)'),
            ('Ignacio Flores (Parque La Libertad)', 'Ignacio Flores (Parque La Libertad)'),
            # Añade más parroquias de Latacunga si es necesario
        )),
        ('Salcedo', (
            ('San Miguel', 'San Miguel'),
            ('Antonio José Holguín (Santa Lucía)', 'Antonio José Holguín (Santa Lucía)'),
            # Añade más parroquias de Salcedo si es necesario
        )),
        ('Pujilí', (
            ('San Francisco de Pujilí', 'San Francisco de Pujilí'),
            ('Alaques (Alaquez)', 'Alaques (Alaquez)'),
            # Añade más parroquias de Pujilí si es necesario
        )),
        # Añade más cantones de Cotopaxi con sus respectivas parroquias si es necesario
    )

    PARROQUIAS_ESMERALDAS = (
        ('Atacames', 'Atacames'),
        ('La Unión', 'La Unión'),
        ('Limones', 'Limones'),
        ('Río Verde', 'Río Verde'),
        ('Tonsupa', 'Tonsupa'),
        # Agrega más parroquias según sea necesario
    )

    PARROQUIAS_GALAPAGOS = (
        ('Puerto Ayora', 'Puerto Ayora'),
        ('Puerto Baquerizo Moreno', 'Puerto Baquerizo Moreno'),
        # Agrega aquí más parroquias según sea necesario
    )

    PARROQUIAS_IMBABURA = (
        ('Ibarra', (
                ('Caranqui', 'Caranqui'),
                ('La Dolorosa del Priorato', 'La Dolorosa del Priorato'),
                ('San Antonio de Ibarra', 'San Antonio de Ibarra'),
                ('San Francisco de Ibarra', 'San Francisco de Ibarra'),
                ('Sagrario', 'Sagrario'),
            )
        ),
        ('Otavalo', (
                ('Dr. Miguel Egas Cabezas', 'Dr. Miguel Egas Cabezas'),
                ('Cotacachi', 'Cotacachi'),
                ('Otavalo', 'Otavalo'),
                ('San José de Quichinche', 'San José de Quichinche'),
                ('San Juan de Ilumán', 'San Juan de Ilumán'),
                ('San Pablo', 'San Pablo'),
            )
        ),
        # Otras parroquias de Imbabura aquí
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    provincia =  models.CharField(choices=PROVINCIA, max_length=200,null=True)
    canton1 = models.CharField(choices=CANTONES_AZUAY, max_length=200,null=True)
    canton2 = models.CharField(choices=CANTONES_BOLIVAR, max_length=200,null=True)
    canton3 = models.CharField(choices=CANTONES_CAÑAR, max_length=200,null=True)
    canton4 = models.CharField(choices=CANTONES_CARCHI, max_length=200,null=True)
    canton5 = models.CharField(choices=CANTONES_CHIMBORAZO, max_length=200,null=True)
    canton6 = models.CharField(choices=CANTONES_COTOPAXI, max_length=200,null=True)
    canton7 = models.CharField(choices=CANTONES_ESMERALDAS, max_length=200,null=True)
    canton8 = models.CharField(choices=CANTONES_GALAPAGOS, max_length=200,null=True)
    canton9 = models.CharField(choices=CANTONES_IMBABURA, max_length=200,null=True)
    canton10 = models.CharField(choices=CANTONES_LOJA, max_length=200,null=True)
    canton11 = models.CharField(choices=CANTONES_LOS_RIOS, max_length=200,null=True)
    canton12 = models.CharField(choices=CANTONES_MANABI, max_length=200,null=True)
    canton13 = models.CharField(choices=CANTONES_MORONA_SANTIAGO, max_length=200,null=True)
    canton14 = models.CharField(choices=CANTONES_NAPO, max_length=200,null=True)
    canton15 = models.CharField(choices=CANTONES_ORELLANA, max_length=200,null=True)
    canton16 = models.CharField(choices=CANTONES_PASTAZA, max_length=200,null=True)
    canton17 = models.CharField(choices=CANTONES_PICHINCHA, max_length=200,null=True)
    canton18 = models.CharField(choices=CANTONES_SANTA_ELENA, max_length=200,null=True)
    canton19 = models.CharField(choices=CANTONES_SANTO_DOMINGO, max_length=200,null=True)
    canton20 = models.CharField(choices=CANTONES_SUCUMBIOS, max_length=200,null=True)
    canton21 = models.CharField(choices=CANTONES_TUNGURAHUA, max_length=200,null=True)
    canton22 = models.CharField(choices=CANTONES_ZAMORA_CHINCHIPE, max_length=200,null=True)
    parroquia1 = models.CharField(choices=PARROQUIAS_AZUAY, max_length=200,null=True)
    parroquia2 = models.CharField(choices=PARROQUIAS_BOLIVAR, max_length=200,null=True)
    parroquia3 = models.CharField(choices=PARROQUIAS_CAÑAR, max_length=200,null=True)
    parroquia4 = models.CharField(choices=CANTONES_CARCHI, max_length=200,null=True)
    parroquia5 = models.CharField(choices=PARROQUIAS_CHIMBORAZO, max_length=200,null=True)
    parroquia6 = models.CharField(choices=PARROQUIAS_COTOPAXI, max_length=200,null=True)
    parroquia7 = models.CharField(choices=PARROQUIAS_ESMERALDAS, max_length=200,null=True)
    parroquia8 = models.CharField(choices=PARROQUIAS_GALAPAGOS, max_length=200,null=True)
    parroquia9 = models.CharField(choices=PARROQUIAS_IMBABURA, max_length=200,null=True)
    direccion = models.CharField( max_length=200,null=True)
    gero_ref = models.CharField( max_length=200,null=True)
    telefono = PhoneNumberField(null=True)

    def __str__(self):
        return 'Contacto de representante legal del usuario: {}'.format(self.user.get_full_name)
    class Meta:
        verbose_name = 'contacto de representante legal de Postulante'
        verbose_name_plural = 'contactos de representante legal de Postulantes'

class activity(models.Model):
    
    DICIPLINAS_ARTISTICAS = (
        ('ARTES ESCÉNICAS', 'ARTES ESCÉNICAS'),
        ('ARTES VISUALES O PLÁSTICAS', 'ARTES VISUALES O PLÁSTICAS'),
        ('ARTES MUSICALES', 'ARTES MUSICALES'),
        ('ARTES AUDIOVISUALES', 'ARTES AUDIOVISUALES'),
        ('ARTES LITERARIAS', 'ARTES LITERARIAS'),
        ('MUSEOLOGÍA', 'MUSEOLOGÍA'),
        ('MEMORIA SOCIAL Y PATRIMONIO INTANGIBLE', 'MEMORIA SOCIAL Y PATRIMONIO INTANGIBLE'),      # Agrega más parroquias según sea necesario
    )
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    diciplina = models.CharField(choices=DICIPLINAS_ARTISTICAS, max_length=200,null=True, verbose_name = "¿EN QUÉ DISCIPLINA/S ARTÍSTCA/S ENMARCA SUS ACTIVIDADES?")
    experiencia= RichTextField( verbose_name = "DESCRIBA DE MANERA SUCINTA SU EXPERIENCIA EN EL ÁMBITO CULTURAL")
    cv = models.ImageField(upload_to='users/%Y/%m/%d/', blank=True, verbose_name = "Adjunte su curriculum vitale")
    enlace_1 = models.URLField(max_length=200, blank=True,verbose_name = "Escriba la URL de sus trabajos que se encuentren publicados digitalmente")
    enlace_2 = models.URLField(max_length=200, blank=True,verbose_name = "Escriba la URL de sus trabajos que se encuentren publicados digitalmente")
    enlace_3 = models.URLField(max_length=200, blank=True,verbose_name = "Escriba la URL de sus trabajos que se encuentren publicados digitalmente")
    ruac = models.BooleanField(default=False, verbose_name = "¿ES PARTE DEL REGISTRO ÚNICO DE ARTISTAS Y GESTORES CULTURALES - RUAC ?") 
    agremiacion = models.BooleanField(default=False, verbose_name = "¿PERTENECE A ALGUNA AGREMIACIÓN / COLECTIVO ?") 
    nombre_agremiacion = models.CharField(max_length=200,null=True, verbose_name = "Si pertenece a una agremiación o colectivo, escriba el nombre")

    class Meta:
        verbose_name = 'actividad cultural del Postulante'
        verbose_name_plural = 'actividades culturales del Postulante'

    def __str__(self):
        return 'Actividades Culturales de usuario: {}'.format(self.user.get_full_name)
    

class terms(models.Model):
    user = models.OneToOneField(settings.AUTH_USER_MODEL, on_delete=models.CASCADE,null=True)
    agree = models.BooleanField(default=False, verbose_name = "Estoy deacuerdo con los términos y condiciones del contrato.") 
    aprueba = models.BooleanField(default=False, verbose_name = "El postulante aprobó la declaratoria") 
    class Meta:
        verbose_name = 'Validaciones de declaratorías del los postulantes'
        verbose_name_plural = 'Validación de declaratoría del postulante'

    def __str__(self):
        return 'Declaratoría del postulante: {}'.format(self.user.get_full_name)
    
    def save(self, *args, **kwargs):
        if  self.agree is True:
            self.agree = self.aprueba
        super(terms, self).save(*args, **kwargs)
    
    def get_absolute_url(self):
            return reverse('account:aprobe', args=[self.id, self.aprueba])
 




