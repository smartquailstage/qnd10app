# Generated by Django 4.2.6 on 2024-03-19 17:57

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('Fomento_Editorial', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='course',
            name='actividad',
            field=models.BooleanField(blank=True, null=True, verbose_name='Estado de la actividad de la convocatoría'),
        ),
        migrations.AddField(
            model_name='course',
            name='fecha_inicio',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='course',
            name='fecha_vencimiento',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='course',
            name='students',
            field=models.ManyToManyField(blank=True, related_name='courses_joined', to=settings.AUTH_USER_MODEL, verbose_name='Usuarios Postulantes'),
        ),
        migrations.AlterField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='Fomento_Editorial.subject', verbose_name='Categoría de convocatoria'),
        ),
        migrations.AlterField(
            model_name='course',
            name='title',
            field=models.CharField(max_length=200, verbose_name='Nombre de Convocatoria'),
        ),
    ]
