# -*- coding: utf-8 -*-
# Generated by Django 1.10.8 on 2017-12-21 19:05
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('faceusers', '0004_auto_20171220_1343'),
    ]

    operations = [
        migrations.RenameField(
            model_name='faceusers',
            old_name='post_reactions_anger_total',
            new_name='post_reactions_angry_total',
        ),
    ]
