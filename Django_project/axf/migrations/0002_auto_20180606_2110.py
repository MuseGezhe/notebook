# -*- coding: utf-8 -*-
# Generated by Django 1.11.4 on 2018-06-06 13:10
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('axf', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='addresses',
            name='detail_address',
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AlterField(
            model_name='addresses',
            name='province',
            field=models.CharField(max_length=20, null=True),
        ),
    ]
