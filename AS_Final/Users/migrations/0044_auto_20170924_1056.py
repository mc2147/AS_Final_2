# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-09-24 10:56
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('Users', '0043_auto_20170924_1036'),
    ]

    operations = [
        migrations.AlterField(
            model_name='subworkout',
            name='Template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.SubWorkout_Template'),
        ),
    ]
