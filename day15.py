##Write a function to calculate the factorial of a number.


def factorial_number(number):
	factorial = 1
	for i in range (number,0, -1):
		factorial *= i 

	
	print(f"{factorial} is factorial numer of {number}")


if __name__ == '__main__':
	number = int(input("Enter a number : "))
	factorial_number(number)