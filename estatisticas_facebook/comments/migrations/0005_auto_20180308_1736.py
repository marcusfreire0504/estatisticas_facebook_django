# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-03-08 17:36
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('comments', '0004_comment_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='comment',
            name='message',
            field=models.CharField(default='', max_length=18000),
        ),
    ]
