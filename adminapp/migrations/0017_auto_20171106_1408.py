# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-06 20:08
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('adminapp', '0016_remove_alumno_tipo_persona'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('numid', models.CharField(max_length=15)),
                ('nombre', models.CharField(max_length=50)),
                ('apellido', models.CharField(max_length=50)),
                ('domicilio', models.CharField(max_length=100)),
                ('telefono', models.CharField(blank=True, max_length=9, null=True)),
                ('ocupacion', models.CharField(max_length=70)),
                ('fecha_nacimiento', models.DateField(blank=True, null=True)),
                ('edad', models.IntegerField(blank=True, null=True)),
                ('condicion', models.CharField(blank=True, max_length=100, null=True)),
                ('grado_anterior', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='GradoAnterior', to='adminapp.GradoAnterior')),
                ('grupo_etnico', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.GrupoEtnico')),
                ('municipio', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Municipio')),
                ('sexo', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Sexo')),
                ('tipo_persona', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='TipoPersona', to='adminapp.TipoPersona')),
                ('trabaja', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='trabaja', to='adminapp.Descicion')),
                ('usuario', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, related_name='Persona', to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='grado_anterior',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='grupo_etnico',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='municipio',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='sexo',
        ),
        migrations.RemoveField(
            model_name='alumno',
            name='trabaja',
        ),
        migrations.RemoveField(
            model_name='promotor',
            name='grupo_etnico',
        ),
        migrations.RemoveField(
            model_name='promotor',
            name='municipio',
        ),
        migrations.RemoveField(
            model_name='promotor',
            name='sexo',
        ),
        migrations.AddField(
            model_name='facilitador',
            name='usuario',
            field=models.OneToOneField(default=1, on_delete=django.db.models.deletion.CASCADE, related_name='Facilitador', to=settings.AUTH_USER_MODEL),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='centro',
            name='promotor',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='adminapp.Persona'),
        ),
        migrations.AlterField(
            model_name='grado',
            name='facilitador',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='matricula',
            name='persona',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Persona'),
        ),
        migrations.AlterUniqueTogether(
            name='grado',
            unique_together=set([('grado', 'horario', 'facilitador')]),
        ),
        migrations.DeleteModel(
            name='Alumno',
        ),
        migrations.DeleteModel(
            name='Promotor',
        ),
    ]