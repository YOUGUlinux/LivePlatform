# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 12:15
from __future__ import unicode_literals

import backend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0005_auto_20170803_2013'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liveroom',
            name='file_path',
            field=models.CharField(default='tempDIR/', max_length=50),
        ),
        migrations.AlterField(
            model_name='liveroom',
            name='thumbnail_path',
            field=models.ImageField(default='default_thumbnail.jpg', upload_to=backend.models.get_file_path),
        ),
    ]