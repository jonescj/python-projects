# Writing to a file
with open("example.txt", 'w') as file:
	file.write("Hello, World!")

# Appending to a file
with open("example.txt", 'a') as file:
	file.write("\nThis is an appended line.")