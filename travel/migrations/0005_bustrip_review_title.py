# -*- coding: utf-8 -*-
# Generated by Django 1.9.5 on 2016-05-10 16:27
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('travel', '0004_auto_20160510_1901'),
    ]

    operations = [
        migrations.AddField(
            model_name='bustrip',
            name='review_title',
            field=models.CharField(default='Review Title', max_length=64),
        ),
    ]
