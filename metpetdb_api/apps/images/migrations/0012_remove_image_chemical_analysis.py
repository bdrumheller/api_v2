# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-08-27 02:29
from __future__ import unicode_literals

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0011_auto_20180826_1618'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='image',
            name='chemical_analysis',
        ),
    ]
