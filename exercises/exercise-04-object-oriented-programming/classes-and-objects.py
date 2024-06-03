# Define a class Car with attributes for make, model, and year. Include a method to display the car's information.

class Car:
	def __init__(self, make, model, year):
		self.make = make
		self.model = model
		self.year = year

	def display(self):
		print(f"This car is a {self.year} {self.make} {self.model}.")

car = Car("Nisson", "Sentra", 2024)
car.display()


# Create an object of the Car class and call the method to display its information.

class Bus(Car):

	def display(self):
		print(f"This is a {self.year} {self.make} {self.model} bus.")

bus = Bus("Jelcz","Single-Deck",2024)
bus.display()