# Generated by Django 4.2.6 on 2024-03-14 13:22

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('announ', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('account', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='fomento_categorias',
            name='categoria',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='announ_categoria_created', to='announ.categorias_linea_fomento_editorial'),
        ),
        migrations.AddField(
            model_name='fomento_categorias',
            name='fomento',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='announ_created', to='announ.categoria_linea_fomento_editorial'),
        ),
        migrations.AddField(
            model_name='edit_profile_done',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contacto_legal',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contacto',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='contact_profile',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='activity',
            name='user',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
