# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-11-27 14:03
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0032_auto_20171123_0813'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='configuracion',
            name='fin_clases',
        ),
        migrations.RemoveField(
            model_name='configuracion',
            name='inicio_clases',
        ),
        migrations.RemoveField(
            model_name='configuracion',
            name='periodo',
        ),
        migrations.AddField(
            model_name='periodo',
            name='fin_clases',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='periodo',
            name='inicio_clases',
            field=models.DateField(blank=True, null=True),
        ),
    ]