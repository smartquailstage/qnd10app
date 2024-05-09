# Generated by Django 4.2.12 on 2024-05-09 22:57

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0005_alter_project_proceso'),
    ]

    operations = [
        migrations.CreateModel(
            name='BibliographicReference',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('authors', models.CharField(max_length=255)),
                ('publication_year', models.PositiveIntegerField()),
                ('journal', models.CharField(blank=True, max_length=255, null=True)),
                ('volume', models.CharField(blank=True, max_length=50, null=True)),
                ('issue', models.CharField(blank=True, max_length=50, null=True)),
                ('pages', models.CharField(blank=True, max_length=50, null=True)),
                ('doi', models.CharField(blank=True, max_length=100, null=True)),
                ('url', models.URLField(blank=True, null=True)),
                ('abstract', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.RemoveField(
            model_name='project',
            name='portada',
        ),
        migrations.AlterField(
            model_name='project',
            name='overview',
            field=models.TextField(help_text='Identificación de un debate o giro paradigmático y explicación sobre cómo cada uno de los capítulos que compondrán el tomo representan lo dicho.', verbose_name='Resumen breve del proyecto de tomo'),
        ),
        migrations.AlterField(
            model_name='project',
            name='subject',
            field=models.ForeignKey(help_text='Seleccione la categoría de la convocatoria en la que desea postular', on_delete=django.db.models.deletion.CASCADE, related_name='proyectos_subject', to='proyectos.subject', verbose_name='Nombre de categoría de convocatoria a la que se desea postular'),
        ),
        migrations.AlterField(
            model_name='project',
            name='title',
            field=models.CharField(max_length=300, verbose_name='Título del proyecto'),
        ),
    ]
