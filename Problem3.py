number = 600851475143 
i = 2
# Devides the number by i^x until it's not a factor
# Then it moves to another number
while i * i <= number:
	if number % i:
		i += 1
	else:
		number //= i
		
print (number)