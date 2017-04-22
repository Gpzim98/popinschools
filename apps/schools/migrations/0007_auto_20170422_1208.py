# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-22 12:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0006_alreadystudiedhere'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'ordering': ('-date',)},
        ),
        migrations.AddField(
            model_name='school',
            name='work_time',
            field=models.CharField(blank=True, help_text='Inform the working time', max_length=300, null=True, verbose_name='Working time'),
        ),
    ]