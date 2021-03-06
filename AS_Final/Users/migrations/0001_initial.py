# -*- coding: utf-8 -*-
# Generated by Django 1.11 on 2017-10-02 16:43
from __future__ import unicode_literals

import datetime
from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Exercise',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Video_Description', models.CharField(default='', max_length=1000)),
                ('New_Code', models.CharField(default='', max_length=20)),
                ('Code', models.CharField(default='', max_length=20)),
                ('Name', models.CharField(default='', max_length=200)),
                ('Type', models.CharField(default='', max_length=200)),
                ('Level', models.IntegerField(default=0)),
                ('Bodyweight', models.BooleanField(default=False)),
                ('Tempo', models.BooleanField(default=False)),
                ('Tempo_Value', models.CharField(default='', max_length=10)),
                ('Pause', models.CharField(default='', max_length=10)),
                ('Description_Code', models.CharField(default='', max_length=20)),
            ],
        ),
        migrations.CreateModel(
            name='Member',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Picture', models.FileField(default='', upload_to='static/user_profile_pictures')),
                ('Level', models.IntegerField(default=1)),
                ('Admin', models.BooleanField(default=False)),
                ('New', models.BooleanField(default=True)),
                ('Signup_Date', models.DateTimeField(null=True)),
                ('Expiry_Date', models.DateTimeField(null=True)),
                ('Paid', models.BooleanField(default=False)),
                ('Agreed', models.BooleanField(default=False)),
                ('Read', models.BooleanField(default=False)),
                ('Has_Workouts', models.BooleanField(default=False)),
                ('Finished_Workouts', models.BooleanField(default=False)),
                ('DOB', models.CharField(default='', max_length=10)),
                ('Height', models.CharField(default='', max_length=10)),
                ('Weight', models.CharField(default='', max_length=10)),
                ('Squat', models.DecimalField(decimal_places=1, default=0, max_digits=4, null=True)),
                ('Bench', models.DecimalField(blank=True, decimal_places=1, default=0, max_digits=4, null=True)),
                ('D_Lift', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('OP', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('PC', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('CJerk', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('Snatch', models.DecimalField(decimal_places=1, default=0, max_digits=4)),
                ('Other', models.CharField(default='', max_length=1000)),
                ('Training_Time', models.CharField(default='', max_length=30)),
                ('Primary_Sports', models.CharField(default='', max_length=300)),
                ('Prior_RPE', models.BooleanField(default=False)),
                ('User', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
        migrations.CreateModel(
            name='Set',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Sets', models.IntegerField(default=0)),
                ('Code', models.CharField(default='', max_length=2)),
                ('Exercise_Type', models.CharField(default='', max_length=200)),
                ('Level', models.IntegerField(default=0)),
                ('Reps', models.IntegerField(default=0)),
                ('Rest_Time', models.DurationField(default=datetime.timedelta(0, 120))),
                ('Order', models.IntegerField(default=0)),
                ('Exercise', models.OneToOneField(blank=True, default='', null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='Stat',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Type', models.CharField(default='', max_length=200)),
                ('Exercise_Name', models.CharField(default='', max_length=200)),
                ('Max', models.IntegerField(default=0)),
                ('Suggested_Weight', models.IntegerField(default=0)),
                ('Alloy_Weight', models.IntegerField(default=0)),
                ('Updated', models.BooleanField(default=False)),
                ('Alloy_Reps', models.IntegerField(default=0)),
                ('Alloy_Performance_Reps', models.IntegerField(default=0)),
                ('Level_Up', models.BooleanField(default=False)),
                ('Core', models.BooleanField(default=True)),
                ('Level', models.IntegerField(default=0)),
                ('Failed', models.BooleanField(default=False)),
                ('Member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='Stats', to='Users.Member')),
            ],
        ),
        migrations.CreateModel(
            name='SubWorkout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Filled_Sets', models.IntegerField(default=0)),
                ('Special_Sets', models.BooleanField(default=False)),
                ('Show_Alloy', models.BooleanField(default=False)),
                ('Alloy_Weight', models.IntegerField(default=0)),
                ('Alloy_Passed', models.BooleanField(default=False)),
                ('Maxed_Sets', models.BooleanField(default=False)),
                ('Stopped', models.BooleanField(default=False)),
                ('Dropped', models.BooleanField(default=False)),
                ('Stop_Sets', models.IntegerField(default=0)),
                ('Drop_Sets', models.IntegerField(default=0)),
                ('Set_Stats', models.CharField(default='', max_length=300)),
                ('Suggested_Weight', models.IntegerField(default=0)),
                ('Drop_Weight', models.IntegerField(default=0)),
                ('Submitted', models.BooleanField(default=False)),
                ('Exercise', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.Exercise')),
            ],
        ),
        migrations.CreateModel(
            name='SubWorkout_Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Exercise_Type', models.CharField(blank=True, default='', max_length=200, null=True)),
                ('Sets', models.IntegerField(default=0)),
                ('Reps', models.CharField(default='', max_length=10)),
                ('Stop_Set', models.BooleanField(default=False)),
                ('Drop_Set', models.BooleanField(default=False)),
                ('Strength_Stop', models.IntegerField(default=0)),
                ('Strength_Drop', models.IntegerField(default=0)),
                ('Special_Reps', models.CharField(default='', max_length=10)),
                ('Order', models.IntegerField(default=0)),
                ('RPE', models.CharField(default='', max_length=3)),
                ('Deload', models.IntegerField(default=0)),
                ('Alloy', models.BooleanField(default=False)),
                ('Alloy_Reps', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Tags', models.CharField(default='', max_length=300)),
                ('Title', models.CharField(default='', max_length=200)),
                ('File', models.FileField(upload_to='static/videos/')),
                ('Has_Thumbnail', models.BooleanField(default=False)),
                ('Thumbnail', models.FileField(default=None, upload_to='Thumbnails')),
                ('Exercise_Type', models.CharField(default='', max_length=200)),
                ('Description', models.CharField(default='', max_length=1000)),
                ('Default_Thumbnail_URL', models.CharField(default='/static/videos/Thumbnails/Default_Thumbnail.png', max_length=100)),
                ('Level_Access', models.IntegerField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name='Workout',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Current_Block', models.BooleanField(default=True)),
                ('Completed', models.BooleanField(default=False)),
                ('Show_Alloy_Weights', models.BooleanField(default=False)),
                ('Alloy', models.BooleanField(default=False)),
                ('Alloy_Passed', models.BooleanField(default=False)),
                ('Last_Alloy', models.BooleanField(default=False)),
                ('Last_Workout', models.BooleanField(default=False)),
                ('Submitted', models.BooleanField(default=False)),
                ('Level', models.IntegerField(default=0)),
                ('Ordered_ID', models.IntegerField(default=0)),
                ('Week', models.IntegerField(default=0)),
                ('Day', models.IntegerField(default=0)),
                ('Date', models.DateField(auto_now=True)),
                ('_Date', models.CharField(default='', max_length=10)),
                ('Member', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='workouts', to='Users.Member')),
                ('Sets', models.ManyToManyField(blank=True, default='', null=True, to='Users.Set')),
                ('SubWorkouts', models.ManyToManyField(default='', to='Users.SubWorkout')),
            ],
        ),
        migrations.CreateModel(
            name='Workout_Template',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Level_Group', models.IntegerField(default=0)),
                ('Level', models.IntegerField(default=0)),
                ('Ordered_ID', models.IntegerField(default=0)),
                ('Week', models.IntegerField(default=0)),
                ('Day', models.IntegerField(default=0)),
                ('_Date', models.CharField(default='', max_length=10)),
                ('Block_Num', models.IntegerField(default=0)),
                ('Block', models.CharField(default='', max_length=200)),
                ('Alloy', models.BooleanField(default=False)),
                ('First', models.BooleanField(default=False)),
                ('Block_End', models.BooleanField(default=False)),
                ('Last', models.BooleanField(default=False)),
                ('Has_Tempo', models.BooleanField(default=False)),
                ('SubWorkouts', models.ManyToManyField(default='', to='Users.SubWorkout_Template')),
            ],
        ),
        migrations.AddField(
            model_name='workout',
            name='Template',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='Users.Workout_Template'),
        ),
        migrations.AddField(
            model_name='subworkout',
            name='Template',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='Users.SubWorkout_Template'),
        ),
        migrations.AddField(
            model_name='exercise',
            name='Video',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.PROTECT, related_name='exercises', to='Users.Video'),
        ),
    ]
