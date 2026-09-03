##Write a program that checks if a given input year is a leap year or not

def is_leap_year(year):
	return year % 400 == 0 or(
		year % 4 == 0 and  year % 100 != 0)


if __name__ == '__main__':
	year = int(input("Enter a year : "))
	if is_leap_year(year) is True:
		print(f"{year} is leap") 
	else:
		print(f"{year} is not leap")