# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2020-03-01 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('album', '0002_auto_20200301_1323'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='editor',
            options={},
        ),
        migrations.AddField(
            model_name='editor',
            name='phone_number',
            field=models.CharField(blank=True, max_length=10),
        ),
    ]
