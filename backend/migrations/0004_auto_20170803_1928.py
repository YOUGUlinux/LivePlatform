# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-08-03 11:28
from __future__ import unicode_literals

import backend.models
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('backend', '0003_auto_20170803_1902'),
    ]

    operations = [
        migrations.AlterField(
            model_name='liveroom',
            name='slide_path',
            field=models.FileField(default='default_slide.jpg', upload_to=backend.models.get_file_path),
        ),
        migrations.AlterField(
            model_name='liveroom',
            name='thumbnail_path',
            field=models.ImageField(default='default_thumbnail.jpg', upload_to=backend.models.get_file_path),
        ),
    ]