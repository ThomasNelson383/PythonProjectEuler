end = 4000000
sum = 0
# getting all the even Fibonacci sequences
seqO = 1
seqC = 1
while seqC < end:
	temp = seqC
	seqC = seqC + seqO
	seqO = temp
	if seqO % 2 == 0:
		sum += seqO
		
print (sum)