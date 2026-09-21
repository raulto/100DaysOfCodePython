#Write a function to find the intersection of two lists.


def list_inserction(a,b):
	new_list = list_a + list_b
	new_list_norepetidos= list(set(new_list))
	new_list_repetidos= []
	for i in range(0,len(new_list_norepetidos)):
		count = 0
		for x in new_list:
			if new_list_norepetidos[i] == x:
				count +=1
			if count >= 2:
				new_list_repetidos.append(x)
				break
					

	print(new_list_repetidos)
			



					


if __name__ == '__main__':
	list_a = [1, 2, 3, 4,4,10]
	list_b = [3, 4, 5, 6,3,3]
	list_inserction(list_a,list_b)