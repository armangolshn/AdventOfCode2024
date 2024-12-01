inputData = list()
# Reading the input file

# with open("Sample_01_Day_01.txt", "r") as file:
# 	for line in file:
# 		inputData.append(line.rsplit())

with open("Input_01_Day_01.txt", "r") as file:
	for line in file:
		inputData.append(line.rsplit())

# Part 01
# Calculating the total distance between the left numbers and the right numbers

# Dividing the input data into two lists and sorting them
listLeft = [item[0] for item in inputData]
listLeft.sort()

listRight = [item[1] for item in inputData]
listRight.sort()

if(len(listLeft) != len(listRight)):
  print("The number of elements in the two lists are not equal")
else:
	distance = 0
	for i in range(len(listLeft)):
		distance += abs(int(listLeft[i]) - int(listRight[i]))
	print("Total Distance is: ", distance)
# Answer is 2 066 446

# Part 02
# Calculating the similarity score
itemSimilarityScore = 0
totalSimilarityScore = 0

# print("List Left: ", listLeft)
# print("List Right: ", listRight)

for item in listLeft:
	for occurence in listRight:
		if item == occurence:
			itemSimilarityScore += 1
	# print("For Item: ", item, "Similarity Score is: ", item, " * ", itemSimilarityScore)
	totalSimilarityScore += int(item) * itemSimilarityScore
	itemSimilarityScore = 0

print("Total Similarity Score is: ", totalSimilarityScore)
# Answer is 24 931 009