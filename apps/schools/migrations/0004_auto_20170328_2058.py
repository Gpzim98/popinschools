# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-28 20:58
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0003_auto_20170328_2053'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='eventsoffered',
            name='accomodation',
        ),
        migrations.AddField(
            model_name='school',
            name='accomodation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.Accommodation'),
        ),
    ]
