# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-02 10:50
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0062_auto_20171002_1025'),
    ]

    operations = [
        migrations.AddField(
            model_name='video',
            name='Has_Thumbnail',
            field=models.BooleanField(default=False),
        ),
    ]