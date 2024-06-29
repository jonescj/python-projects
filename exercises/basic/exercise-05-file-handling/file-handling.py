# Write a program that writes a list of your favorite quotes to a file.

with open("example.txt", 'w') as file:
	file.write("I am a file!")
	file.write("\nI was a file!")
	file.write("\nI am now not a file!")
	file.write("\nI was never a file!")

# Write a program that reads the contents of the file and prints each quote.

with open("example.txt", 'r') as file:
	content = file.read()
	print(content)