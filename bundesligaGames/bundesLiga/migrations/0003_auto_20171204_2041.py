# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 20:41
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bundesLiga', '0002_auto_20171204_1951'),
    ]

    operations = [
        migrations.RenameField(
            model_name='teamranks',
            old_name='еqual1',
            new_name='draws',
        ),
    ]
