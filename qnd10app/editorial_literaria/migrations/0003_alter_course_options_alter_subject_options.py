# Generated by Django 4.2.11 on 2024-04-17 19:58

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('editorial_literaria', '0002_manualpostulacion'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='course',
            options={'ordering': ['-created'], 'verbose_name_plural': 'Convocatorias'},
        ),
        migrations.AlterModelOptions(
            name='subject',
            options={'ordering': ['title'], 'verbose_name_plural': 'Modulos de Convocatoria'},
        ),
    ]
