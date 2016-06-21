# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-09 19:24
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0002_auto_20160509_2203'),
    ]

    operations = [
        migrations.AddField(
            model_name='bustrip',
            name='fare',
            field=models.IntegerField(default=22000, help_text='=/ tsh'),
        ),
        migrations.AlterField(
            model_name='bustrip',
            name='bus_company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='travel.BusCompany'),
        ),
    ]
