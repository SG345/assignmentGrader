# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-21 09:57
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0006_announcements'),
    ]

    operations = [
        migrations.DeleteModel(
            name='Staff',
        ),
        migrations.RemoveField(
            model_name='userprofile',
            name='profile_pic',
        ),
        migrations.AlterField(
            model_name='announcements',
            name='an_id',
            field=models.AutoField(default='0', editable=False, primary_key=True, serialize=False),
        ),
        migrations.AlterField(
            model_name='problems',
            name='problem_id',
            field=models.AutoField(default='0', editable=False, primary_key=True, serialize=False),
        ),
    ]
