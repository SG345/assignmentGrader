# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 11:06
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0022_auto_20160131_1027'),
    ]

    operations = [
        migrations.AlterField(
            model_name='leaderboard',
            name='lb_score',
            field=models.IntegerField(),
        ),
    ]
