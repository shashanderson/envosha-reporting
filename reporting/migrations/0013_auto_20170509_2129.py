# -*- coding: utf-8 -*-
# Generated by Django 1.11.1 on 2017-05-09 13:29
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0012_remove_parameter_company'),
    ]

    operations = [
        migrations.AlterField(
            model_name='parameter',
            name='area_personal_type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='reporting.AreaPersonalType'),
        ),
    ]