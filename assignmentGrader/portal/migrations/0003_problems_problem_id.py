# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-15 14:09
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0002_auto_20160115_1357'),
    ]

    operations = [
        migrations.AddField(
            model_name='problems',
            name='problem_id',
            field=models.TextField(default=1),
            preserve_default=False,
        ),
    ]