class BankAccount:
	""" Initializing the account of user."""
	def __init__(self, account_number, account_holder, balance=0.0):
		self.account_holder = account_holder
		self.account_number = account_number
		self.balance = balance

	def deposit(self, amount):
		"""Performs deposit of amounts by users."""
		if amount > 0:
			self.balance += amount
		else:
			return "Invalid deposit amount"

	def withdraw(self, amount):
		"""Performs the withdrawal of amount by users."""
		if 0 < amount <= self.balance:
			self.balance -= amount
		else:
			return f"Invalid withdrawal, Low balance: {self.balance}"

	def __str__(self):
		return f"Withdrawn: {self.amount} Balance: {self.balance}."

