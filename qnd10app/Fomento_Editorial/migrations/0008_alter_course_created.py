# Generated by Django 4.2.6 on 2024-03-20 15:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Fomento_Editorial', '0007_alter_course_fecha_inicio_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='course',
            name='created',
            field=models.DateField(auto_now_add=True),
        ),
    ]
