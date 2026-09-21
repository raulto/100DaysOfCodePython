#Handle exceptions for file not found.

def select_file():
	try:
		with open('test.txt','r') as file:
			print(file.read())
	except FileNotFoundError:
		print("No se encontro file")


if __name__ == '__main__':
	select_file()