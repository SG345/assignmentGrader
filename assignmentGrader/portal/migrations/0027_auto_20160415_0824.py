# -*- coding: utf-8 -*-
# Generated by Django 1.9.1 on 2016-04-15 08:24
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('portal', '0026_auto_20160318_0729'),
    ]

    operations = [
        migrations.CreateModel(
            name='AdminAccess',
            fields=[
                ('admin_id', models.AutoField(primary_key=True, serialize=False)),
                ('staff_code', models.TextField()),
            ],
        ),
        migrations.AddField(
            model_name='problems',
            name='expected_timelimit',
            field=models.TextField(default=5),
        ),
    ]
