# -*- coding: utf-8 -*-
# Generated by Django 1.11.5 on 2017-12-06 15:33
from __future__ import unicode_literals

import datetime
from django.db import migrations, models
from django.utils.timezone import utc


class Migration(migrations.Migration):

    dependencies = [
        ('article', '0004_auto_20171206_2333'),
    ]

    operations = [
        migrations.AlterField(
            model_name='articlepost',
            name='created',
            field=models.DateTimeField(default=datetime.datetime(2017, 12, 6, 15, 33, 55, 931498, tzinfo=utc)),
        ),
    ]