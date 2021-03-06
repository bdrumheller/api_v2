# -*- coding: utf-8 -*-
# Generated by Django 1.11.10 on 2018-06-19 04:53
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('images', '0006_auto_20180619_0335'),
    ]

    operations = [
        migrations.CreateModel(
            name='XrayImage',
            fields=[
                ('image', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, primary_key=True, serialize=False, to='images.Image')),
                ('element', models.CharField(blank=True, max_length=256, null=True)),
                ('dwelltime', models.SmallIntegerField(blank=True, null=True)),
                ('current', models.SmallIntegerField(blank=True, null=True)),
                ('voltage', models.SmallIntegerField(blank=True, null=True)),
            ],
            options={
                'db_table': 'xray_image',
                'ordering': ('image_id',),
            },
        ),
    ]
