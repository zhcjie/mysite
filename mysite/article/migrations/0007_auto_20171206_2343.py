# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-06 15:43
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0006_auto_20171206_2341'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=django.utils.timezone.now),
        ),
    ]
