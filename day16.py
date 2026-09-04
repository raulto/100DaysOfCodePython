##Write a function to check if a given string is a palindrome.

def is_palíndromo(text):
	new_text = ""
	for x in range(len(text)-1, -1, -1):
		new_text += text[x]

	return new_text.lower() == text

		

if __name__=='__main__':
	name = input("Enter a name: ").lower()

	if is_palíndromo(name.lower()):
		print("El nombre es palydromo")
	else:
		print("No lo es")
