# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-13 16:54
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0024_remove_centro_tipo_centro'),
    ]

    operations = [
        migrations.AlterField(
            model_name='facilitador',
            name='centro',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='adminapp.Centro'),
        ),
    ]