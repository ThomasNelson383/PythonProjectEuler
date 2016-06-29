topNumber = 20
endNumber = 1

for num in range (2, topNumber):
	endNumber *= num

smallestNumber = endNumber
for number in range(topNumber, endNumber, topNumber):
	test = True
	for i in range(topNumber-1, 1, -1):
		if number % i != 0:
			test = False
			break;
	
	if test:
		smallestNumber = number
		break


print (smallestNumber)