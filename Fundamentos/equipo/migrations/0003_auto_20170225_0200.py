# -*- coding: utf-8 -*-
# Generated by Django 1.10.5 on 2017-02-25 07:00
from __future__ import unicode_literals

import datetime
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('equipo', '0002_auto_20170225_0125'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='cargo',
            name='tipo',
        ),
        migrations.AddField(
            model_name='cargo',
            name='nombre',
            field=models.CharField(default=datetime.date(2017, 2, 25), max_length=50),
            preserve_default=False,
        ),
    ]