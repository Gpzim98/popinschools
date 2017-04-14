# -*- coding: utf-8 -*-
# Generated by Django 1.10.6 on 2017-04-13 23:17
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('profile', '0001_initial'),
        ('schools', '0005_auto_20170413_2237'),
    ]

    operations = [
        migrations.CreateModel(
            name='AlreadyStudiedHere',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('school', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='schools.School')),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='profile.Profile')),
            ],
        ),
    ]
