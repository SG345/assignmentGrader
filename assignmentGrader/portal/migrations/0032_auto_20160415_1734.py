# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-15 17:34
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0031_auto_20160415_1721'),
    ]

    operations = [
        migrations.AlterField(
            model_name='problems',
            name='current_etime',
            field=models.TextField(default=5),
        ),
        migrations.AlterField(
            model_name='submissions',
            name='submit_etime',
            field=models.TextField(default=0),
        ),
    ]