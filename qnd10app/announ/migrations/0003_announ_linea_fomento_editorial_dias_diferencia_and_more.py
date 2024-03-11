# Generated by Django 4.2.6 on 2024-03-11 04:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('announ', '0002_announ_linea_fomento_editorial_portada'),
    ]

    operations = [
        migrations.AddField(
            model_name='announ_linea_fomento_editorial',
            name='dias_diferencia',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='announ_linea_fomento_editorial',
            name='fecha_vencimiento',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='announ_linea_fomento_editorial',
            name='horas_diferencia',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='announ_linea_fomento_editorial',
            name='minutos_diferencia',
            field=models.DateTimeField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='announ_linea_fomento_editorial',
            name='segundos_diferencia',
            field=models.DateTimeField(blank=True, null=True),
        ),
    ]
