# Generated by Django 2.2.8 on 2019-12-24 15:37

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Intereses',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Categoria', models.CharField(max_length=50)),
                ('Nombre', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('fecha_creacion', models.DateTimeField(auto_now_add=True)),
                ('lugar', models.CharField(max_length=100)),
                ('descripcion', models.CharField(max_length=300)),
                ('tipo', models.CharField(choices=[('Abierto', 'Abierto'), ('Cerrado', 'Cerrado')], max_length=30)),
                ('usario_añadido', models.ManyToManyField(related_name='usuario_añadido2', to=settings.AUTH_USER_MODEL)),
                ('usuario_creador', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
