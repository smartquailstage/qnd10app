# Generated by Django 4.2.11 on 2024-04-11 04:28

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('usuarios', '0003_profile_autoidentificacion_profile_genero_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='activity',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='activity',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='date_of_birth',
        ),
        migrations.RemoveField(
            model_name='contacts',
            name='photo',
        ),
        migrations.RemoveField(
            model_name='legal',
            name='date_of_birth',
        ),
        migrations.AlterField(
            model_name='profile',
            name='autoidentificacion',
            field=models.CharField(blank=True, choices=[('SI', 'Sí'), ('NO', 'No')], help_text='¿Usted pertenece a un pueblo o nacionalidad indígena, montubio o afro-ecuatoriano?', max_length=3, null=True, verbose_name='¿Usted pertenece a un pueblo o nacionalidad indígena, montubio o afro-ecuatoriano?'),
        ),
        migrations.CreateModel(
            name='DeclaracionVeracidad',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('acepta_terminos_condiciones', models.BooleanField(default=False, verbose_name='Acepta los Términos y Condiciones de Uso')),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Nombre de Usuario')),
            ],
        ),
    ]
