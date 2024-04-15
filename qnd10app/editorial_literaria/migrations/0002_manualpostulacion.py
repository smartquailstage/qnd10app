# Generated by Django 4.2.11 on 2024-04-15 20:42

import ckeditor.fields
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('editorial_literaria', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='ManualPostulacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Crear Convocatoria', 'Crear Convocatoria'), ('Editar Convocatoria', 'Editar Convocatoria'), ('Mis Convocatorias', 'Mis Convocatorias'), ('inscripción', 'inscripción'), ('Mis Postulaciones', 'Mis Postulaciones'), ('Crear Proyecto', 'Crear Proyecto'), ('Editar Proyecto', 'Editar Proyecto'), ('Mis Proyectos', 'Mis Proyectos')], max_length=100, verbose_name='Selecione el tipo de manual')),
                ('titulo', models.CharField(max_length=100)),
                ('informacion_basica', ckeditor.fields.RichTextField()),
                ('bloque_1', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_2', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_3', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_4', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_5', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('link', models.URLField()),
            ],
        ),
    ]
