# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-02-07 00:11
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('polls', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='independent',
            name='job',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to='polls.Job'),
        ),
        migrations.AlterField(
            model_name='independent',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
