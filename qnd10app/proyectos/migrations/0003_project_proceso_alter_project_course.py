# Generated by Django 4.2.12 on 2024-05-07 04:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('editorial_literaria', '0005_remove_course_projects'),
        ('proyectos', '0002_project_course'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='proceso',
            field=models.CharField(blank=True, choices=[('Aprobado', 'Aprobado'), ('Activo', 'Activo'), ('Subsanacion', 'Subsanacion'), ('Rechazado', 'Rechazado')], help_text='Elija el proceso en la que se encuentra esta postulacion', max_length=255, null=True, verbose_name='Proceso del proyecto postulado'),
        ),
        migrations.AlterField(
            model_name='project',
            name='course',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='proyectos_course', to='editorial_literaria.course', verbose_name='Elija la convocatoria que desea postular este proyecto.'),
        ),
    ]
