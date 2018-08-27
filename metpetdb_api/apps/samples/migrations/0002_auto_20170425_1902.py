# -*- coding: utf-8 -*-
# Generated by Django 1.9 on 2017-04-25 19:02
from __future__ import unicode_literals

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('samples', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='BulkUpload',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.AlterField(
            model_name='subsample',
            name='owner',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='subsamples', to=settings.AUTH_USER_MODEL),
        ),
    ]