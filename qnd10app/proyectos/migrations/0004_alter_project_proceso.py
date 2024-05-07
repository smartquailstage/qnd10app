# Generated by Django 4.2.12 on 2024-05-07 04:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0003_project_proceso_alter_project_course'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='proceso',
            field=models.CharField(blank=True, choices=[('Aprobado', 'Aprobado'), ('Activo', 'Activo'), ('Subsanacion', 'Subsanacion'), ('Rechazado', 'Rechazado')], default='Activo', help_text='Elija el proceso en la que se encuentra esta postulacion', max_length=255, null=True, verbose_name='Proceso del proyecto postulado'),
        ),
    ]
