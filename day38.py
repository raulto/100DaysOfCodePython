#Create a custom exception class.

class CustomException(Exception):
	"""Exception raised for custom error scenarios"""

	def __init__(self, message):
		self.message = message
		super().__init__(self.message)

def validation_name(name):
	
		if name != "Raul":
			raise CustomException("no es raul")

		print("Correcto")
	

if __name__ == '__main__':
	name = input("Escribe Raul: ")
	validation_name(name)
