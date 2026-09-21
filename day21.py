##Write a function to reverse a list.

def reverse_list(numbers):
	new_list = []
	for x in range(len(numbers)-1,-1,-1):
		new_list.append(numbers[x])
	return new_list



if __name__ == '__main__':
	numbers=[5,6,70,43,12,1,65]
	print(reverse_list(numbers))