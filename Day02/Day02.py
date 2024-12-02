inputData = list()

# Reading the input file
# with open("Sample_01_Day_02.txt", "r") as file:
# 	for line in file:
# 		inputData.append(line.rsplit())

with open("Input_01_Day_02.txt", "r") as file:
	for line in file:
		inputData.append(line.rsplit())

def checkSafeReports(report):
	safeReport = False
	increasingList = list()
	decreasingList = list()

	for item in range(len(report)-1):
		if(int(report[item]) > int(report[item + 1]) and int(report[item]) - int(report[item + 1]) <= 3):
			increasingList.append(True)
			decreasingList.append(False)
		elif(int(report[item]) < int(report[item + 1]) and int(report[item + 1]) - int(report[item]) <= 3):
			decreasingList.append(True)
			increasingList.append(False)
		else:
			increasingList.append(False)
			decreasingList.append(False)

	if(all(increasingList) == True or all(decreasingList) == True):
		safeReport = True
	
	return safeReport

# Part 01
safeReportsCount = 0
for report in inputData:
	safeReportsCount += checkSafeReports(report)

print("Number of Safe Reports are: ", safeReportsCount) #Answer is 202

# Part 02
safeReportsCount = 0
for report in inputData:
	safeReportsCount += checkSafeReports(report) or any(checkSafeReports(report[:item] + report[item + 1:]) for item in range(len(report)))

print("Number of Safe Reports are: ", safeReportsCount) #Answer is 271