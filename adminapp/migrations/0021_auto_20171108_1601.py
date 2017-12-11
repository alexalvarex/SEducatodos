# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-08 22:01
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0020_auto_20171107_1453'),
    ]

    operations = [
        migrations.CreateModel(
            name='Familiar',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numid', models.CharField(blank=True, max_length=15, null=True)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('domicilio', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=9, null=True)),
                ('ocupacion', models.CharField(blank=True, max_length=70, null=True)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('familiar', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Familiar', to='adminapp.Alumno')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Municipio')),
                ('parentezco', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Parentezco', to='adminapp.Parentezco')),
                ('sexo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Sexo')),
                ('trabaja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Trabajo', to='adminapp.Descicion')),
            ],
        ),
        migrations.RemoveField(
            model_name='persona',
            name='familiar',
        ),
        migrations.RemoveField(
            model_name='persona',
            name='parentezco',
        ),
        migrations.AlterField(
            model_name='centro',
            name='cada_cuando',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='centro',
            name='donde_funciona',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='centro',
            name='patro_recibe',
            field=models.CharField(blank=True, max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='persona',
            name='ocupacion',
            field=models.CharField(blank=True, max_length=70, null=True),
        ),
    ]