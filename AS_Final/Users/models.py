# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from django.db import models
import datetime
from django.contrib.auth.models import User, Group

class Member(models.Model):
	User = models.OneToOneField(User)
	Picture = models.FileField(upload_to='User_Profile_Pictures', max_length=100, default="")
	Level = models.IntegerField(default=1)
	# Checks
	Admin = models.BooleanField(default=False)
	New = models.BooleanField(default=True)
	Signup_Date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
	Expiry_Date = models.DateTimeField(auto_now=False, auto_now_add=False, null=True)
	Paid = models.BooleanField(default=False)
	Agreed = models.BooleanField(default=False)
	Read = models.BooleanField(default=False)
	Has_Workouts = models.BooleanField(default=False)
	Finished_Workouts = models.BooleanField(default=False)
	# Stats
	DOB = models.CharField(max_length=10, default= "")
	Height = models.CharField(max_length=10, default= "")
	Weight = models.CharField(max_length=10, default= "")
	# Lifts
	Squat = models.DecimalField(max_digits=4, decimal_places=1, default=0, null=True)
	Bench = models.DecimalField(max_digits=4, decimal_places=1, default=0, null=True, blank=True)
	D_Lift = models.DecimalField(max_digits=4, decimal_places=1, default=0)
	OP = models.DecimalField(max_digits=4, decimal_places=1, default=0)
	PC = models.DecimalField(max_digits=4, decimal_places=1, default=0)
	CJerk = models.DecimalField(max_digits=4, decimal_places=1, default=0)
	Snatch = models.DecimalField(max_digits=4, decimal_places=1, default=0)
	Other = models.CharField(max_length=1000, default= "")
	# Training Experience
	Training_Time = models.CharField(max_length=30, default= "")
	Primary_Sports = models.CharField(max_length=300, default= "")
	Prior_RPE = models.BooleanField(default=False)

class Stat(models.Model):
	Type = models.CharField(default="", max_length=200)
	Member = models.ForeignKey(Member, related_name="Stats")
	Exercise_Name = models.CharField(default="", max_length=200)
	Max = models.IntegerField(default=0)
	Suggested_Weight = models.IntegerField(default=0)
	Alloy_Weight = models.IntegerField(default=0)
	Updated = models.BooleanField(default=False)
	Alloy_Reps = models.IntegerField(default=0)
	Alloy_Performance_Reps = models.IntegerField(default=0)
	Level_Up = models.BooleanField(default=False)
	Core = models.BooleanField(default=True)
	Level = models.IntegerField(default=0)
	Failed = models.BooleanField(default=False)
	def Reset(self):
		self.Failed = False
		self.Updated = False
		self.Level_Up = False
		self.Max = 0
		self.save()
	# Email
class Video(models.Model):
	Tags = models.CharField(default = "", max_length=300)
	Title = models.CharField(default = "", max_length=200)
	File = models.FileField(upload_to='Videos', max_length=100)
	Has_Thumbnail = models.BooleanField(default=False)
	Thumbnail = models.FileField(upload_to='Thumbnails', max_length=100, default=None)
	# Exercises = models.ManyToManyField(Exercise, default="", related_name="Video")
	# Thumbnail = models.FileField(upload_to='static/videos/Thumbnails', max_length=100)
	Exercise_Type = models.CharField(default="", max_length=200)
	Description = models.CharField(default="", max_length=1000)
	Default_Thumbnail_URL = models.CharField(default="/static/videos/Thumbnails/Default_Thumbnail.png", max_length=100)
	Level_Access = models.IntegerField(default=0)
	def Give_Access(Level_Num):
		if self.Level_Access <= Level_Num:
			return True
		else:
			return False
	def Get_Thumbnail(self):
		if self.Has_Thumbnail:
			return "/" + self.Thumbnail.url
		else:
			return "/static/videos/Thumbnails/Default_Thumbnail.png"

# Specific exercise as in 'All Levels'
class Exercise(models.Model):
	# ID = models.CharField(default="", max_length=20)
	Video = models.ForeignKey(Video, blank=True, null=True, related_name="exercises", on_delete=models.PROTECT)
	Video_Description = models.CharField(default="", max_length = 1000)
	New_Code = models.CharField(default="", max_length=20)
	Code = models.CharField(default="", max_length=20)
	Name = models.CharField(default="", max_length=200)
	Type = models.CharField(default="", max_length=200)
	Level = models.IntegerField(default=0)
	Bodyweight = models.BooleanField(default=False)
	Tempo = models.BooleanField(default=False)
	Tempo_Value = models.CharField(default="", max_length=10)
	Pause = models.CharField(default="", max_length=10)
	Description_Code = models.CharField(default="", max_length=20)


class Set(models.Model):
	Sets = models.IntegerField(default=0)
	Code = models.CharField(default="", max_length=2) # Level + Exercise Type
	Exercise = models.OneToOneField(Exercise, default="", null=True, blank=True)
	Exercise_Type = models.CharField(default="", max_length=200)
	Level = models.IntegerField(default=0)
	Reps = models.IntegerField(default=0)
	Rest_Time = models.DurationField(default=datetime.timedelta(minutes=2, seconds=0))
	Order = models.IntegerField(default=0)

# Row in each table in 'Program'
class SubWorkout_Template(models.Model):
	Exercise_Type = models.CharField(default="", max_length=200, null=True, blank=True)
	Sets = models.IntegerField(default=0)
	Reps = models.CharField(default="", max_length=10)
	Stop_Set = models.BooleanField(default=False) 
	Drop_Set = models.BooleanField(default=False) 
	Strength_Stop = models.IntegerField(default=0)
	Strength_Drop = models.IntegerField(default=0)
	Special_Reps = models.CharField(default="", max_length=10)	
	Order = models.IntegerField(default=0)
	RPE = models.CharField(default="", max_length=3)
	Deload = models.IntegerField(default=0)
	Alloy = models.BooleanField(default=False)
	Alloy_Reps = models.IntegerField(default=0)
	# Workout = models.OneToOneField(Workout, default="")  
	# Exercise = models.OneToOneField(Exercise, default="", null=True, blank=True)
	# Alloy = models.BooleanField(default=False)
	# Alloy_Reps = models.IntegerField(default=0)
class SubWorkout(models.Model):	
	Exercise = models.ForeignKey(Exercise, on_delete=models.CASCADE, blank=True, null=True)
	Template = models.ForeignKey(SubWorkout_Template, on_delete=models.CASCADE, blank=True, null=True)
	Suggested_Weight = models.IntegerField(default=0)
	Filled_Sets = models.IntegerField(default=0)

	Special_Sets = models.BooleanField(default=False)

	Show_Alloy = models.BooleanField(default=False)
	Alloy_Weight = models.IntegerField(default=0)
	Alloy_Passed = models.BooleanField(default=False)

	Maxed_Sets = models.BooleanField(default=False) 
	
	Stopped = models.BooleanField(default=False)
	Dropped = models.BooleanField(default=False)

	Stop_Sets = models.IntegerField(default=0)
	Drop_Sets = models.IntegerField(default=0)

	Set_Stats = models.CharField(default="", max_length=300)
	
	Suggested_Weight = models.IntegerField(default=0)
	Drop_Weight = models.IntegerField(default=0)
	
	Submitted = models.BooleanField(default=False)

class Workout_Template(models.Model):
	Level_Group = models.IntegerField(default=0)
	Level = models.IntegerField(default=0)
	Ordered_ID = models.IntegerField(default=0)
	Week = models.IntegerField(default=0)
	Day = models.IntegerField(default=0)
	SubWorkouts = models.ManyToManyField(SubWorkout_Template, default="")
	_Date = models.CharField(default="", max_length=10)
	Block_Num = models.IntegerField(default=0)
	Block = models.CharField(default="", max_length=200)
	Alloy = models.BooleanField(default=False)
	First = models.BooleanField(default=False)
	Block_End = models.BooleanField(default=False)
	Last = models.BooleanField(default=False)
	Has_Tempo = models.BooleanField(default=False)

class Workout(models.Model):
	Current_Block = models.BooleanField(default=True)
	Completed = models.BooleanField(default=False)
	Show_Alloy_Weights = models.BooleanField(default=False)
	Alloy = models.BooleanField(default=False)
	Alloy_Passed = models.BooleanField(default=False)
	Last_Alloy = models.BooleanField(default=False)
	Last_Workout = models.BooleanField(default=False)
	Member = models.ForeignKey(Member, related_name="workouts")
	Submitted = models.BooleanField(default=False)
	Template = models.ForeignKey(Workout_Template)
	Level = models.IntegerField(default=0)
	Ordered_ID = models.IntegerField(default=0)
	Week = models.IntegerField(default=0)
	Day = models.IntegerField(default=0)
	Sets = models.ManyToManyField(Set, default="", null=True, blank=True)
	Date = models.DateField(auto_now=True)
	_Date = models.CharField(default="", max_length=10)
	SubWorkouts = models.ManyToManyField(SubWorkout, default="")
	# _User = models.OneToOneField(User, null=True)
