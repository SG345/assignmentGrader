# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-15 10:33
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0028_submissions_submit_etime'),
    ]

    operations = [
        migrations.AddField(
            model_name='adminaccess',
            name='max_attempts',
            field=models.IntegerField(default=3),
        ),
        migrations.AddField(
            model_name='problems',
            name='current_etime',
            field=models.TextField(default=5),
        ),
    ]
