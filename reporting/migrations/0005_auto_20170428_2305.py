# -*- coding: utf-8 -*-
# Generated by Django 1.10.1 on 2017-04-28 15:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('reporting', '0004_auto_20170428_2304'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='Type',
            new_name='AreaPersonalType',
        ),
    ]
