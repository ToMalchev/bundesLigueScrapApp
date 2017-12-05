# -*- coding: utf-8 -*-
# Generated by Django 1.11.7 on 2017-12-04 17:59
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Match',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('team1', models.CharField(max_length=50)),
                ('team2', models.CharField(max_length=50)),
                ('goals_team1', models.IntegerField()),
                ('goals_team2', models.IntegerField()),
                ('date', models.CharField(max_length=100)),
                ('match_id', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='TeamRanks',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('win', models.IntegerField()),
                ('loss', models.IntegerField()),
                ('еqual', models.IntegerField()),
                ('points', models.IntegerField()),
            ],
        ),
    ]
