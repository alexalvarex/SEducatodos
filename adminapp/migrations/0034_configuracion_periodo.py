# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-27 14:16
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0033_auto_20171127_0803'),
    ]

    operations = [
        migrations.AddField(
            model_name='configuracion',
            name='periodo',
            field=models.ForeignKey(default=1, on_delete=django.db.models.deletion.CASCADE, to='adminapp.Periodo'),
            preserve_default=False,
        ),
    ]
