# -*- coding: utf-8 -*-
# Generated by Django 1.11.17 on 2019-01-23 02:01
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('rango', '0002_auto_20190121_2032'),
    ]

    operations = [
        migrations.AddField(
            model_name='category',
            name='slug',
            field=models.SlugField(default=0),
            preserve_default=False,
        ),
    ]
