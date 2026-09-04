#Write a program to check if a number is even or odd.

def main(number):
	
	if number % 2 == 0 :
		print(f"{number} is even")
		return
	
	print(f"{number} is odd")

if __name__ == "__main__":
	number = int(input("Enter a number: "))
	main(number)
