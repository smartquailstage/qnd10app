# Generated by Django 4.2.12 on 2024-05-10 04:11

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('proyectos', '0012_cv_delete_file'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cv',
            old_name='cv',
            new_name='file',
        ),
    ]