# Generated by Django 4.2.12 on 2024-05-09 05:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0005_alter_legal_telefono_contacto'),
    ]

    operations = [
        migrations.AlterField(
            model_name='activity',
            name='nombre_agremiacion',
            field=models.CharField(blank=True, help_text='Si pertence a una agremiación artistica, escriba el nombre de la misma. Caso contrario, deje el campo en blanco. ', max_length=255, null=True, verbose_name='Nombre de la Agremiación'),
        ),
    ]