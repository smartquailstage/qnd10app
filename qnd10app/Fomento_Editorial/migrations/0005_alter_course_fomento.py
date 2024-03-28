# Generated by Django 4.2.6 on 2024-03-19 22:38

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Fomento_Editorial', '0004_fomento_alter_subject_options_alter_course_subject_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='fomento',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, related_name='fomento', to='Fomento_Editorial.fomento', verbose_name='Línea de fomento'),
        ),
    ]
