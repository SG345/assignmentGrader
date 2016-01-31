# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-01-31 09:37
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0019_auto_20160131_0858'),
    ]

    operations = [
        migrations.AddField(
            model_name='restrictions',
            name='allow',
            field=models.TextField(default=True),
        ),
        migrations.AlterField(
            model_name='submissions',
            name='submit_score',
            field=models.IntegerField(default=0),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='student_score',
            field=models.IntegerField(default=0),
        ),
    ]
