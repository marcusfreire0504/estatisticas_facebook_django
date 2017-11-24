# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-11-24 22:12
from __future__ import unicode_literals

from django.db import migrations, models
import django.utils.timezone


class Migration(migrations.Migration):

    dependencies = [
        ('pages', '0005_auto_20171120_1534'),
    ]

    operations = [
        migrations.AddField(
            model_name='page',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='pageinsights',
            name='created',
            field=models.DateTimeField(auto_now_add=True, default=django.utils.timezone.now),
            preserve_default=False,
        ),
    ]
