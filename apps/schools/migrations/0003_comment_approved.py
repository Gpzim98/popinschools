# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 18:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0002_comment'),
    ]

    operations = [
        migrations.AddField(
            model_name='comment',
            name='approved',
            field=models.BooleanField(default=True),
        ),
    ]
