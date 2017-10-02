# -*- coding: utf-8 -*-
# Generated by Django 1.11.3 on 2017-10-02 22:29
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('core', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='object_uuid',
        ),
        migrations.AddField(
            model_name='profile',
            name='picture_url',
            field=models.URLField(blank=True),
        ),
    ]
