# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-03-29 14:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0004_auto_20170328_2058'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='videos',
            name='url',
        ),
        migrations.AddField(
            model_name='videos',
            name='embeded_code',
            field=models.TextField(default=''),
        ),
    ]
