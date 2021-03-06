# Generated by Django 3.2.8 on 2022-04-27 00:58

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('libreria', '0006_rename_animales_animal'),
    ]

    operations = [
        migrations.CreateModel(
            name='vacuna',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=100, null=True, verbose_name='Nombre')),
                ('fecha', models.DateField(max_length=100, null=True, verbose_name='Direccion')),
                ('vacuna_animal', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='libreria.animal')),
            ],
        ),
    ]
