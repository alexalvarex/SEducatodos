# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-10-20 14:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('adminapp', '0010_auto_20171020_0730'),
    ]

    operations = [
        migrations.AlterField(
            model_name='matricula',
            name='requisito',
            field=models.FileField(upload_to='imagenes'),
        ),
    ]