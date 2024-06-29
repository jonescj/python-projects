# Write a program that iterates from 1 to 10 and uses break to exit the loop when it reaches 5.

for n in range(1,11):
	print(n)
	if n == 5:
		break

# Write a program that iterates from 1 to 10 and uses continue to skip even numbers.

for n in range(1,11):
	if n % 2 == 0:
		continue 
	print(n)