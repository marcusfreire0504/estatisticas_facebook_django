# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2018-07-04 13:39
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('posts', '0013_auto_20180704_1325'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='post',
            name='post_reactions_negativo_porcentagem',
        ),
        migrations.RemoveField(
            model_name='post',
            name='post_reactions_positivo_porcentagem',
        ),
    ]
