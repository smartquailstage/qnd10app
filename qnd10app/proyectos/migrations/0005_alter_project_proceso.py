# Generated by Django 4.2.12 on 2024-05-07 05:09

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0004_alter_project_proceso'),
    ]

    operations = [
        migrations.AlterField(
            model_name='project',
            name='proceso',
            field=models.CharField(blank=True, choices=[('Aprobado', 'Aprobado'), ('Activo', 'Activo'), ('Subsanación', 'Subsanación'), ('Rechazado', 'Rechazado')], default='Activo', help_text='Elija el proceso en la que se encuentra esta postulacion', max_length=255, null=True, verbose_name='Proceso del proyecto postulado'),
        ),
    ]