# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-29 09:08
from __future__ import unicode_literals

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0055_subworkout_drop_weight'),
    ]

    operations = [
        migrations.AddField(
            model_name='member',
            name='Agreed',
            field=models.BooleanField(default=False),
        ),
    ]