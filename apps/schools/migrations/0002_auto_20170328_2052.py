# -*- coding: utf-8 -*-
# Generated by Django 1.10 on 2017-03-28 20:52
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('schools', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Acomodation',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('is_beakfest_included', models.BooleanField(default=False, help_text='Is BreakFest Included?', verbose_name='Is BreakFeast included?')),
                ('is_lunch_included', models.BooleanField(default=False, help_text='Is lunch Included?', verbose_name='Is Lunch included?')),
                ('is_dinner_included', models.BooleanField(default=False, help_text='Is dinner Included?', verbose_name='Is Dinner Included?')),
                ('is_tv_in_the_bedroom', models.BooleanField(default=False, help_text='Do you have a tv in the bedroom?', verbose_name='Do you have a tv in the bedroom?')),
                ('is_wardrobe_in_the_bedroom', models.BooleanField(default=False, help_text='Do you have a wardrobe in the bedroom?', verbose_name='Do you have a wardrobe in the bedroom?')),
                ('is_air_in_the_badroom', models.BooleanField(default=False, help_text='Do you have a air conditioning in the bedroom?', verbose_name='Do you have a air conditioning in the bedroom?')),
                ('duration', models.CharField(help_text='Time of acomodation', max_length=255, verbose_name='Period of stay in')),
                ('wifi_free', models.BooleanField(default=False, help_text='Do you have free wifi?', verbose_name='Do you have free wifi?')),
                ('time_to_school', models.CharField(help_text='How much time it take from the school?', max_length=255, verbose_name='How much time it take from the school?')),
                ('differentials', models.CharField(help_text="What is your accomodation's differential", max_length=255, verbose_name='Tell Me about your differentials')),
            ],
        ),
        migrations.AlterField(
            model_name='school',
            name='refounds',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Refounds', max_digits=10, null=True, verbose_name='Redounds'),
        ),
        migrations.AlterField(
            model_name='school',
            name='registration_fee',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='Registration Fee Price', max_digits=10, null=True, verbose_name='Registration Fee Price'),
        ),
        migrations.AlterField(
            model_name='school',
            name='workbook',
            field=models.DecimalField(blank=True, decimal_places=2, default=0, help_text='HWorkbook Price', max_digits=10, null=True, verbose_name='Workbook Price'),
        ),
        migrations.AddField(
            model_name='eventsoffered',
            name='accomodation',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='schools.Acomodation'),
        ),
    ]
