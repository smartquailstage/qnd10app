# Generated by Django 4.2.13 on 2024-05-31 00:02

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('actividades_espacio_publico', '0004_rename_usuario_evento_10000_user_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='evento_30000',
            name='user',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Nombre de Usuario'),
        ),
    ]
