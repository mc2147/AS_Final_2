import math

RPE_Dict = {10: [100, 94, 91, 89, 86,84,82, 80,78,76,75,73,71,70,68,67,66,64,63,62,61,60,59,58,57],
9.5: [97, 94, 91, 89, 86, 84, 82, 80, 78, 76, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56],
9: [97, 94, 91, 89, 86, 84, 82, 80, 78, 76, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56],
8.5: [94, 91, 89, 86, 84, 82, 80, 78, 76, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55],
8: [91, 89, 86, 84, 82, 80, 78, 76, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54],
7.5: [88, 86, 84, 82, 80, 78, 76, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53],
7: [86, 84, 82, 80, 78, 76, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52],
6: [84, 82, 80, 78, 76, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51.5],
5: [84, 82, 80, 78, 76, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51.5],
4: [82, 80, 78, 76, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51.5, 51],
3: [80, 78, 76, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51.5, 51, 50],
2: [78, 76, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51.5, 51, 50],
1: [77, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51.5, 51, 50],
} 

def Get_Weight(Max, Reps, RPE):
	Weight = 0	
	if isinstance(RPE, str):
		if re.search("-", RPE) != None:
			RPE = int(RPE[0])
			print("New RPE: ")
	if str(RPE) not in RPE_String_Dict:
		RPE = math.floor(float(RPE))
	_RPE = str(RPE)

	Percentage = RPE_String_Dict[_RPE][Reps - 1]
	
	Weight = Percentage*Max/100

	Rounded_Weight = Weight - (Weight % 5)
	# return RPE_Dict[RPE][Reps - 1]
	return Rounded_Weight
	# return 0

def Get_Max(Weight, Reps, RPE):
	if isinstance(RPE, str):
		if re.search("-", RPE) != None:
			RPE = int(RPE[0])
			print("New RPE: ")
	if str(RPE) not in RPE_String_Dict:
		RPE = math.floor(float(RPE))
	_RPE = str(RPE)

	Percentage = RPE_String_Dict[_RPE][Reps - 1]
	print("Percentage: " + str(Percentage))
	# print("")
	Max = (Weight*100)/Percentage
	return Max

# RPEs = [["1-2", 1], ["3-4", 3], ["5-6", 5], ["7", 7], ["8", 8], ["8.5", 8.5], ["9", 9], ["9.5", 9.5], ["10", 10]]

RPE_String_Dict = {"10.0": [100, 94, 91, 89, 86,84,82, 80,78,76,75,73,71,70,68,67,66,64,63,62,61,60,59,58,57],
"9.0": [97, 94, 91, 89, 86, 84, 82, 80, 78, 76, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56],
"8.5": [94, 91, 89, 86, 84, 82, 80, 78, 76, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55],
"8.0": [91, 89, 86, 84, 82, 80, 78, 76, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54],
"7.5": [88, 86, 84, 82, 80, 78, 76, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53],
"7.0": [86, 84, 82, 80, 78, 76, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52],
"6.0": [84, 82, 80, 78, 76, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51.5],
"5.0": [84, 82, 80, 78, 76, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51.5],
"4.0": [82, 80, 78, 76, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51.5, 51],
"3.0": [80, 78, 76, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51.5, 51, 50],
"2.0": [78, 76, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51.5, 51, 50],
"1.0": [77, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51.5, 51, 50],
"0.0": [77, 75, 73, 71, 70, 68, 67, 66, 64, 63, 62, 61, 60, 59, 58, 57, 56, 55, 54, 53, 52, 51.5, 51, 50],
} 
