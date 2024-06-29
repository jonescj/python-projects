# Create a dictionary with information about a book (title, author, year). Add a new key-value pair for the genre, and print the updated dictionary.

book = {
	"title": "TITLE",
	"author": "AUTHOR",
	"year": "YEAR"
}

print(book)

# Write a program that iterates through the dictionary and prints each key and value.

for key, value in book.items():
	print(key+":"+value)