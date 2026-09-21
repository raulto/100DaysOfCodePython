#Write a function to calculate the Fibonacci sequence up to a certain limit.

def fibonnaci_serie(count):
	fibonacci_list = [0,1]
	for x in range(0,count):
		fibonacci_list.append(fibonacci_list[x] + (fibonacci_list[x+1]))
	return fibonacci_list

if __name__ == '__main__':
	count = int(input("How many times would you like repeat the fibonacci serie: "))
	print(fibonnaci_serie(count))
