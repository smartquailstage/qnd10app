# Generated by Django 4.2.12 on 2024-05-07 00:36

import ckeditor.fields
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import editorial_literaria.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('contenttypes', '0002_remove_content_type_name'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('proyectos', '__first__'),
    ]

    operations = [
        migrations.CreateModel(
            name='Course',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('portada', models.ImageField(blank=True, upload_to='portada/%Y/%m/%d/', verbose_name='Foto de portada de convocatoria')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
                ('overview', models.TextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses_created', to=settings.AUTH_USER_MODEL)),
                ('projects', models.ManyToManyField(blank=True, related_name='projects_joined', to='proyectos.project')),
                ('students', models.ManyToManyField(blank=True, related_name='courses_joined', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Convocatorias',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='ManualCrearProyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Crear Convocatoria', 'Crear Convocatoria'), ('Editar Convocatoria', 'Editar Convocatoria'), ('Mis Convocatorias', 'Mis Convocatorias'), ('inscripción', 'inscripción'), ('Mis Postulaciones', 'Mis Postulaciones'), ('Crear Proyecto', 'Crear Proyecto'), ('Editar Proyecto', 'Editar Proyecto'), ('Mis Proyectos', 'Mis Proyectos')], max_length=100, verbose_name='Selecione el tipo de manual')),
                ('titulo', models.CharField(max_length=100)),
                ('informacion_basica', ckeditor.fields.RichTextField()),
                ('bloque_1', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_2', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_3', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_4', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_5', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ManualCreateConvocatoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Crear Convocatoria', 'Crear Convocatoria'), ('Editar Convocatoria', 'Editar Convocatoria'), ('Mis Convocatorias', 'Mis Convocatorias'), ('inscripción', 'inscripción'), ('Mis Postulaciones', 'Mis Postulaciones'), ('Crear Proyecto', 'Crear Proyecto'), ('Editar Proyecto', 'Editar Proyecto'), ('Mis Proyectos', 'Mis Proyectos')], max_length=100, verbose_name='Selecione el tipo de manual')),
                ('titulo', models.CharField(max_length=100)),
                ('informacion_basica', ckeditor.fields.RichTextField()),
                ('bloque_1', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_2', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_3', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_4', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_5', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ManualEditConvocatoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Crear Convocatoria', 'Crear Convocatoria'), ('Editar Convocatoria', 'Editar Convocatoria'), ('Mis Convocatorias', 'Mis Convocatorias'), ('inscripción', 'inscripción'), ('Mis Postulaciones', 'Mis Postulaciones'), ('Crear Proyecto', 'Crear Proyecto'), ('Editar Proyecto', 'Editar Proyecto'), ('Mis Proyectos', 'Mis Proyectos')], max_length=100, verbose_name='Selecione el tipo de manual')),
                ('titulo', models.CharField(max_length=100)),
                ('informacion_basica', ckeditor.fields.RichTextField()),
                ('bloque_1', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_2', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_3', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_4', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_5', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ManualEditProyecto',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Crear Convocatoria', 'Crear Convocatoria'), ('Editar Convocatoria', 'Editar Convocatoria'), ('Mis Convocatorias', 'Mis Convocatorias'), ('inscripción', 'inscripción'), ('Mis Postulaciones', 'Mis Postulaciones'), ('Crear Proyecto', 'Crear Proyecto'), ('Editar Proyecto', 'Editar Proyecto'), ('Mis Proyectos', 'Mis Proyectos')], max_length=100, verbose_name='Selecione el tipo de manual')),
                ('titulo', models.CharField(max_length=100)),
                ('informacion_basica', ckeditor.fields.RichTextField()),
                ('bloque_1', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_2', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_3', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_4', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_5', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ManualInscripcion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Crear Convocatoria', 'Crear Convocatoria'), ('Editar Convocatoria', 'Editar Convocatoria'), ('Mis Convocatorias', 'Mis Convocatorias'), ('inscripción', 'inscripción'), ('Mis Postulaciones', 'Mis Postulaciones'), ('Crear Proyecto', 'Crear Proyecto'), ('Editar Proyecto', 'Editar Proyecto'), ('Mis Proyectos', 'Mis Proyectos')], max_length=100, verbose_name='Selecione el tipo de manual')),
                ('titulo', models.CharField(max_length=100)),
                ('informacion_basica', ckeditor.fields.RichTextField()),
                ('bloque_1', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_2', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_3', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_4', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_5', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ManualMisConvocatoria',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Crear Convocatoria', 'Crear Convocatoria'), ('Editar Convocatoria', 'Editar Convocatoria'), ('Mis Convocatorias', 'Mis Convocatorias'), ('inscripción', 'inscripción'), ('Mis Postulaciones', 'Mis Postulaciones'), ('Crear Proyecto', 'Crear Proyecto'), ('Editar Proyecto', 'Editar Proyecto'), ('Mis Proyectos', 'Mis Proyectos')], max_length=100, verbose_name='Selecione el tipo de manual')),
                ('titulo', models.CharField(max_length=100)),
                ('informacion_basica', ckeditor.fields.RichTextField()),
                ('bloque_1', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_2', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_3', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_4', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_5', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ManualMisPostulaciones',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Crear Convocatoria', 'Crear Convocatoria'), ('Editar Convocatoria', 'Editar Convocatoria'), ('Mis Convocatorias', 'Mis Convocatorias'), ('inscripción', 'inscripción'), ('Mis Postulaciones', 'Mis Postulaciones'), ('Crear Proyecto', 'Crear Proyecto'), ('Editar Proyecto', 'Editar Proyecto'), ('Mis Proyectos', 'Mis Proyectos')], max_length=100, verbose_name='Selecione el tipo de manual')),
                ('titulo', models.CharField(max_length=100)),
                ('informacion_basica', ckeditor.fields.RichTextField()),
                ('bloque_1', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_2', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_3', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_4', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_5', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ManualMisProyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Crear Convocatoria', 'Crear Convocatoria'), ('Editar Convocatoria', 'Editar Convocatoria'), ('Mis Convocatorias', 'Mis Convocatorias'), ('inscripción', 'inscripción'), ('Mis Postulaciones', 'Mis Postulaciones'), ('Crear Proyecto', 'Crear Proyecto'), ('Editar Proyecto', 'Editar Proyecto'), ('Mis Proyectos', 'Mis Proyectos')], max_length=100, verbose_name='Selecione el tipo de manual')),
                ('titulo', models.CharField(max_length=100)),
                ('informacion_basica', ckeditor.fields.RichTextField()),
                ('bloque_1', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_2', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_3', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_4', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_5', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='ManualPostulacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(choices=[('Crear Convocatoria', 'Crear Convocatoria'), ('Editar Convocatoria', 'Editar Convocatoria'), ('Mis Convocatorias', 'Mis Convocatorias'), ('inscripción', 'inscripción'), ('Mis Postulaciones', 'Mis Postulaciones'), ('Crear Proyecto', 'Crear Proyecto'), ('Editar Proyecto', 'Editar Proyecto'), ('Mis Proyectos', 'Mis Proyectos')], max_length=100, verbose_name='Selecione el tipo de manual')),
                ('titulo', models.CharField(max_length=100)),
                ('informacion_basica', ckeditor.fields.RichTextField()),
                ('bloque_1', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_1', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_2', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_2', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_3', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_3', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_4', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_4', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('bloque_5', ckeditor.fields.RichTextField(blank=True, null=True)),
                ('image_5', models.ImageField(blank=True, null=True, upload_to='manuales/%Y/%m/%d/', verbose_name='Seleccione una imagen')),
                ('link', models.URLField()),
            ],
        ),
        migrations.CreateModel(
            name='Subject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('slug', models.SlugField(max_length=200, unique=True)),
            ],
            options={
                'verbose_name_plural': 'Modulos de Convocatoria',
                'ordering': ['title'],
            },
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('url', models.URLField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Text',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('content', models.TextField()),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Proyectos',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('titulo', models.CharField(max_length=100)),
                ('informacion_basica', ckeditor.fields.RichTextField()),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('postulante', models.ManyToManyField(blank=True, related_name='projects_joined', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name_plural': 'Convocatorias',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='postulacion',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('postulante', models.ManyToManyField(blank=True, related_name='project_user_joined', to=settings.AUTH_USER_MODEL)),
                ('title', models.ManyToManyField(blank=True, related_name='project_title', to='editorial_literaria.proyectos')),
            ],
            options={
                'verbose_name_plural': 'Proyectos Postulados',
                'ordering': ['-created'],
            },
        ),
        migrations.CreateModel(
            name='Module',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField(blank=True)),
                ('order', editorial_literaria.fields.OrderField(blank=True)),
                ('course', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='modules', to='editorial_literaria.course')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='images')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='File',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=250)),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('updated', models.DateTimeField(auto_now=True)),
                ('file', models.FileField(upload_to='files')),
                ('owner', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='%(class)s_related', to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='course',
            name='subject',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='courses', to='editorial_literaria.subject'),
        ),
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('object_id', models.PositiveIntegerField()),
                ('order', editorial_literaria.fields.OrderField(blank=True)),
                ('content_type', models.ForeignKey(limit_choices_to={'model__in': ('text', 'video', 'image', 'file')}, on_delete=django.db.models.deletion.CASCADE, to='contenttypes.contenttype')),
                ('module', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contents', to='editorial_literaria.module')),
            ],
            options={
                'ordering': ['order'],
            },
        ),
    ]
