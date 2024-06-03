# Define a base class Shape with a method area.

class Shape:
	def __init__(self, width, length):
		self.width = width
		self.length = length

	def area(self):
		print("Need more information...")

# Define a derived class Rectangle that inherits from Shape and implements the area method to calculate the area of a rectangle.

class Rectangle(Shape):

	def area(self):
		print(self.width * self.length)

shape = Shape(3,4)
shape.area()

rectangle = Rectangle(3,4)
rectangle.area()
