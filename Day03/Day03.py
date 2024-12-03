import re
inputData = list()

# Reading the Sample file 1
# with open("Sample_01_Day_03.txt", "r") as file:
# 	inputData = file.read()

#Reading the input file
with open("Input_01_Day_03.txt", "r") as file:
	inputData = file.read()

def multiplication (string):
	result = 0
	validMulSets = re.findall(r'mul\((\d{1,10}),(\d{1,10})\)', string)
	
	for item in validMulSets:
		result += int(item[0]) * int(item[1])
	
	return result

# Part 01
print("Part 01: ", multiplication(inputData)) #Answer is 187 825 547

# Part 02
#Reading the Sample file 2
# with open("Sample_02_Day_03.txt", "r") as file:
# 	inputData = file.read()

# First Try
# inputData = re.sub(r"don't\(\).*?do\(\)",'do()', inputData)
# print("Part 02: ", multiplication(inputData)) #Answer is 87 519 257

# Second Try
#split the input data based on the first occurance of don't() or do()
inputData = re.split(r"don't\(\)", inputData, 1) #based on data to get beginning mul sets
# print(len(inputData)) #must be 2

before = inputData[0]
beforeSumMul = multiplication(before) #315 204

after = "don't()" + inputData[1]
numberOfDont = len(re.findall(r"don't\(\)", after))

doMulList = re.findall(r"do\(\).*?don't\(\)", after)
# print(len(doMulList)) #13

sumList = 0
for item in doMulList:
	sumList += multiplication(item)

print("Part 02: ", sumList + beforeSumMul) #Answer is 85 508 223
	
	



	


