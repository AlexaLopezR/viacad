# -*- coding: utf-8 -*-
# Generated by Django 1.11.6 on 2017-10-27 20:30
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('viacadapp', '0007_remove_registro_costohora'),
    ]

    operations = [
        migrations.AlterField(
            model_name='registro',
            name='contraseña',
            field=models.CharField(max_length=32),
        ),
    ]
