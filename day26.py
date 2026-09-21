#Write a function check if two strings are anagrams.

def check_anagram(a,b):
	list_a = sorted(list(a))
	list_b = sorted(list(b))

	
	print(list_a == list_b)
	


if __name__ == '__main__':
	a = "silent"
	b = "listen"
	check_anagram(a,b)