#Calculate the average of numbers in a text file.

def average_numbers():
	with open("C:\\Users\\RaulT\\Desktop\\promedio-test.txt", "r") as file:
		count = 0
		suma = 0
		for line in file:
			count += 1
			suma += int(line.strip())
		return suma/count

if __name__ == '__main__':
	print("Promedio: ", average_numbers())