# -*- coding: utf-8 -*-
from __future__ import unicode_literals
from .models import *
from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth.decorators import user_passes_test
from django.http import HttpResponse, HttpResponseRedirect, JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, time, timedelta
from django.utils import timezone
from django.contrib.auth import logout, login, authenticate
from django.core.files import File
import json
import stripe     

def User_Ref_Dict(user):
	Dict = {}
	_Member = Member.objects.get(User = user)
	_Level = _Member.Level
	_Workouts = _Member.workouts.all()
	Dict["Member"] = _Member
	Dict["Level"] = _Level
	Dict["Workouts"] = _Workouts
	return Dict

def Check_Level_Up(_Member, Add_Level):
	Level_Up = False
	Curr_Level = _Member.Level
	Stats = _Member.Stats.all()
	
	Squat, Created = Stat.objects.get_or_create(Member = _Member, Type="Squat")
	Bench, Created = Stat.objects.get_or_create(Member = _Member, Type="UB Hor Push")
	Hinge, Created = Stat.objects.get_or_create(Member = _Member, Type="Hinge")
	print("CHECK LEVEL UP FUNCTION:")
	print(Curr_Level)
	if Squat.Level_Up and Bench.Level_Up and Hinge.Level_Up:
		Level_Up = True
	# if Squat.Failed or Bench.Failed or Hinge.Failed:

	if Level_Up:
		print("Member Levelled Up!")
		if Add_Level:
			_Member.Level += 1
			_Member.save()
		return True
	else:
		return False

Days_Of_Week = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']

def Generate_Workouts(Start_Date, Level, Days_List, Member):
	Week_Days = enumerate(Days_Of_Week)
	# Days = Days_List[]
	# Workouts = Workout_Template.objects.get(Level=Level)
	Max_Days = 28
	Output = []
	count = 0
	Days = Days_List
	if Level <= 5:
		if len(Days_List) == 4:
			Days = Days_List[:-1]
		else:
			Days = Days_List
		print("Program Start Date: " + Start_Date.strftime('%m/%d/%Y'))		
		print("Selected Workout Days: ")		
		_Days = []
		for x in Days:
			_Days.append(Days_Of_Week[x])
		print(_Days)

		for i in range(0, 28): #i will be from 1 to 28
			if (Start_Date + timedelta(days=i)).weekday() in Days:
				Workout_Date = Start_Date + timedelta(days=i)
				count += 1				
				string_date = Workout_Date.strftime('%m/%d/%Y')
				_Workout_Template = Workout_Template.objects.get(Level_Group=1, Ordered_ID=count)
				# print("Workout Template: " + "Week " + str(_Workout_Template.Week) + " Day " 
				# + str(_Workout_Template.Day) + " Ordered ID: " + str(_Workout_Template.Ordered_ID) + " Level Group: " + str(_Workout_Template.Level_Group))				
				_Workout = Workout(Template=_Workout_Template, _Date=string_date, Level = Level, Member=Member)
				_Workout.save()
				for x in _Workout.Template.SubWorkouts.all():
					x.Exercise, Created = Exercise.objects.get_or_create(Type = x.Exercise_Type, Level = Level)
					x.save()
					_SubWorkout = SubWorkout(Template = x)
					_SubWorkout.save()
					_Workout.SubWorkouts.add(_SubWorkout)
					_Workout.save()
				print("Level " + str(_Workout.Level) + " Workout Created For: " + _Workout._Date + " (Week " + str(_Workout.Template.Week) + " Day " + str(_Workout.Template.Day) + ")")
				# print(string_date)
				Output.append(string_date)
				# Member.workouts.add(_Workout)
				# Member.save()
		return(Output)
	elif Level <= 10:
		if len(Days_List) == 4:
			Days = Days_List[:-1]
		else:
			Days = Days_List
		Max_Days = 28
		for i in range(0, Max_Days): #i will be from 1 to 28
			if (Start_Date + timedelta(days=i)).weekday() in Days:
				Workout_Date = Start_Date + timedelta(days=i)
				count += 1				
				string_date = Workout_Date.strftime('%m/%d/%Y')
				_Workout_Template = Workout_Template.objects.get(Level_Group=2, Ordered_ID=count)
				_Workout = Workout(Template=_Workout_Template, _Date=string_date, Level = Level, Member=Member)
				_Workout.save()
				for x in _Workout.Template.SubWorkouts.all():
					_SubWorkout = SubWorkout(Template = x)
					_SubWorkout.save()
					_Workout.SubWorkouts.add(_SubWorkout)
					_Workout.save()
				Output.append(string_date)
		return(Output)
	elif Level <= 15: #9 Weeks
		Max_Days = 63
		for i in range(0, Max_Days): #i will be from 1 to 28
			if (Start_Date + timedelta(days=i)).weekday() in Days:
				Workout_Date = Start_Date + timedelta(days=i)
				count += 1				
				string_date = Workout_Date.strftime('%m/%d/%Y')
				if count <= 16:
					_Workout_Template = Workout_Template.objects.get(Level_Group=3, Ordered_ID=count, Block_Num=1)
					_Workout = Workout(Template=_Workout_Template, _Date=string_date, Level = Level, Member=Member)
					_Workout.save()
					for x in _Workout.Template.SubWorkouts.all():
						_SubWorkout = SubWorkout(Template = x)
						_SubWorkout.save()
						_Workout.SubWorkouts.add(_SubWorkout)
					_Workout.save()
				elif count > 16 and count < 36:
					adjusted_count = count - 16
					_Workout_Template = Workout_Template.objects.get(Level_Group=3, Ordered_ID=adjusted_count, Block_Num=2)
					_Workout = Workout(Template=_Workout_Template, _Date=string_date, Level = Level, Member=Member)
					_Workout.save()
					for x in _Workout.Template.SubWorkouts.all():
						_SubWorkout = SubWorkout(Template = x)
						_SubWorkout.save()
						_Workout.SubWorkouts.add(_SubWorkout)
					_Workout.save()
				Output.append(string_date)
		return(Output)
	elif Level <= 25: #9 Weeks
		Max_Days = 63
		for i in range(0, Max_Days): #i will be from 1 to 28
			if (Start_Date + timedelta(days=i)).weekday() in Days:
				Workout_Date = Start_Date + timedelta(days=i)
				count += 1				
				string_date = Workout_Date.strftime('%m/%d/%Y')
				if count <= 16:
					_Workout_Template = Workout_Template.objects.get(Level_Group=4, Ordered_ID=count, Block_Num=1)
					_Workout = Workout(Template=_Workout_Template, _Date=string_date, Level = Level, Member=Member)
					_Workout.save()
					for x in _Workout.Template.SubWorkouts.all():
						_SubWorkout = SubWorkout(Template = x)
						_SubWorkout.save()
						_Workout.SubWorkouts.add(_SubWorkout)
						_Workout.save()
				elif count > 16 and count < 36:
					adjusted_count = count - 16
					_Workout_Template = Workout_Template.objects.get(Level_Group=4, Ordered_ID=adjusted_count, Block_Num=2)
					_Workout = Workout(Template=_Workout_Template, _Date=string_date, Level = Level, Member=Member)
					_Workout.save()
					for x in _Workout.Template.SubWorkouts.all():
						_SubWorkout = SubWorkout(Template = x)
						_SubWorkout.save()
						_Workout.SubWorkouts.add(_SubWorkout)
						_Workout.save()
				Output.append(string_date)
		return(Output)
