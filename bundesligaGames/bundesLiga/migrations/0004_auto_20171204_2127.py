# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 21:27
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('bundesLiga', '0003_auto_20171204_2041'),
    ]

    operations = [
        migrations.RenameField(
            model_name='match',
            old_name='match_id',
            new_name='match_i',
        ),
    ]
