#Write a program to find the largest of three numbers.


def find_largerst_number(numbers):

  temp = numbers[0]
  for i in range(len(numbers)):
    if numbers[i] > temp:
      temp = numbers[i]

  return temp



if __name__ == '__main__':

  numbers = [10, 5, 21]
  biggest_number = find_largerst_number(numbers)
  print(f"{biggest_number} is the biggest number of the list")