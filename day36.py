#Handle exceptions for division by zero.

def division_number(a,b):
	try:
		resultado = a / b 
	except ZeroDivisionError:
		print("no se puede dividr en cero")
	else:
		return resultado

if __name__ == '__main__':
	resultado = division_number(4,0)
	if resultado is None:
		print("No se realizo division")
	else:
		print(resultado)