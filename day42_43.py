#day42: Create a class for a bank account with methods for deposit and withdrawal.
#day43: Implement encapsulation in a class.

class NotHaveFunds(Exception):
	pass

class Account:
	def __init__(self, account_number, funds):
		self.__account_number = account_number
		self.__funds = funds
	def get_account_number(self):
		return self.__account_number


	def get_funds(self):
		return self.__funds


	def deposit(self, amount):
		self.__funds += amount

	def withdrawal(self, amount):
				if amount <= self.__funds:
					self.__funds -= amount
				else:
					raise NotHaveFunds()
