# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-06-21 11:15
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0005_bustrip_review_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='bustrip',
            name='review',
            field=models.TextField(blank=True, max_length=500),
        ),
    ]
