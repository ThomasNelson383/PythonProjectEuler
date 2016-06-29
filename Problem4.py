def isPalindrome(number):
	string = str(number)

	for i in range(0, len(string)):
		if 	string[i] != string[len(string) - 1 - i]:
			return False
	return True

maxPalindrome = 0
maxRight = 100
for leftNumber in range(999, 100, -1):
	if leftNumber <= maxRight :
		break
	for rightNumber in range(leftNumber, 100, -1):
		if rightNumber <= maxRight:
			break
		num = leftNumber * rightNumber
		if isPalindrome(num):
			if maxPalindrome < num :
				maxRight = rightNumber
				maxPalindrome = num

print (maxPalindrome)