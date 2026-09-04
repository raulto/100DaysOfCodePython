#Write a function to count the number of vowels in a string.


vowels = ['a','e','i','o','u']

def count_vowels(text):
	count = 0
	for letter in text:
			if letter in vowels:
				count +=1
	return count

if __name__ == '__main__':
	
	text = input("Enter a text: ").lower().replace(" ","")
	print(count_vowels(text))