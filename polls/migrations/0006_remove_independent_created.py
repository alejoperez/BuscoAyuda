# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-07 04:06
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0005_auto_20160206_2259'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='independent',
            name='created',
        ),
    ]
