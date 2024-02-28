# Generated by Django 4.2.6 on 2024-02-27 19:49

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0011_alter_legal_lucro_jury'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='activity',
            options={'verbose_name': 'actividad cultural del Postulante', 'verbose_name_plural': 'actividades culturales del Postulante'},
        ),
        migrations.AlterModelOptions(
            name='contacto',
            options={'verbose_name': 'Información de contacto de Postulante', 'verbose_name_plural': 'Información de contactos de Postulantes'},
        ),
        migrations.AlterModelOptions(
            name='contacto_legal',
            options={'verbose_name': 'contacto de representante legal de Postulante', 'verbose_name_plural': 'contactos de representante legal de Postulantes'},
        ),
        migrations.AlterModelOptions(
            name='legal',
            options={'verbose_name': 'Estatus legal de Postulante', 'verbose_name_plural': 'Estatus legal de Postulantes'},
        ),
        migrations.AlterModelOptions(
            name='profile',
            options={'verbose_name': 'Perfil de Postulantes', 'verbose_name_plural': 'Perfiles de postulantes'},
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
