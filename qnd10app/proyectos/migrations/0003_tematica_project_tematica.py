# Generated by Django 4.2.13 on 2024-06-04 00:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0002_alter_cv_options_alter_cv_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='tematica',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Temáticas de Convocatoria',
                'ordering': ['title'],
            },
        ),
        migrations.AddField(
            model_name='project',
            name='tematica',
            field=models.ForeignKey(blank=True, help_text='Seleccione la temática de la convocatoria en la que desea postular', null=True, on_delete=django.db.models.deletion.CASCADE, related_name='tematica_subject', to='proyectos.tematica', verbose_name='Nombre de tematica de convocatoria a la que se desea postular'),
        ),
    ]
