#Sort a list of numbers in ascending order.

def sorted_list(numbers):
	return (sorted(numbers))
	

if __name__ == '__main__':
	numbers = [42, 7, 19, 3, 56, 12, 1, 34, 8, 25]
	print(sorted_list(numbers))