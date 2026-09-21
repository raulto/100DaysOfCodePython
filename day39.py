#Create a class for a simple car with methods like start and stop.

class Car:
	def __init__ (self, color, engine, cylinder):
		self.color =color
		self.engine = engine
		self.cylinder = cylinder

	def start(self):
		print("engine start")

	def stop(self):
		print("engine stop")

	def __str__(self):
		return f"{self.color} {self.engine} {self.cylinder}"



if __name__ == '__main__':
	car = Car("red", "GT 250", "4")
	car.start()
	car.stop()
	print(car)
