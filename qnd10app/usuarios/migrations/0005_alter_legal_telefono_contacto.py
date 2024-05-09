# Generated by Django 4.2.12 on 2024-05-09 05:13

import django.core.validators
from django.db import migrations
import phonenumber_field.modelfields


class Migration(migrations.Migration):

    dependencies = [
        ('usuarios', '0004_alter_contacts_perfil_redes_sociales_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='legal',
            name='telefono_contacto',
            field=phonenumber_field.modelfields.PhoneNumberField(default='+593', max_length=128, region=None, validators=[django.core.validators.RegexValidator(message='El número de teléfono debe estar en formato internacional. Ejemplo: +593XXXXXXXXX.', regex='^\\+?593?\\d{9,15}$')], verbose_name='telefono de contacto del representante legal'),
        ),
    ]