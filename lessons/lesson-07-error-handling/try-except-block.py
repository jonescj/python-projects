# Error Handling Example

try:
    result = 10 / 0
except ZeroDivisionError:
    print("Cannot divide by zero!")

try:
    with open('nonexistent_file.txt', 'r') as file:
        content = file.read()
except FileNotFoundError:
    print("File not found!")
