class Calculator:
	"""Initializin the caluclator class"""
	def __init__(self, num1, num2, operation):
		# Instance attributes
		self.num1 = num1
		self.num2 = num2
		self.operation = operation
		
	def add(self):
		"""Performs the addition operation"""
		return self.num1 + self.num2
		
	def subtract(self):
		"""Performs the subtraction operation"""
		return self.num1 - self.num2
		
	def multiply(self):
		"""Performs the multiplication operation"""
		return self.num1 * self.num2
		
	def divide(self):
		"""Performs the division operation"""
		return self.num1 / self.num2
		
	def square(self):
		"""Performs the exponential operation."""
		return pow(self.num1, self.num2)
		
	def calculate(self):
		"""Evaluates user operation choice and reponse accordingly."""
		if self.operation == '+':
			return self.add()
		elif self.operation == '-':
			return self.subtract()
		elif self.operation == '*':
			return self.multiply()
		elif self.operation == '/':
			return self.divide()
		elif self.operation == 'expo':
			return self.square()
		else:
			return "Invalid operation, please try again"
			
	def __str__(self):
		if self.operation == 'expo':
			return f"{self.calculate()}"
		else:
			return f"{self.num1} {self.operation} {self.num2} = {self.calculate()}"
			
def main():
	while True:
		try:
			# Prompting the user for 2 numbers and an operant.
			num1 = int(input("Enter first number: "))
			num2 = int(input("Enter second number: "))
			operation = input("Enter operation ( +, -, *, /, expo): ")
			
			# creating an object for our class. (Instance)
			calc = Calculator( num1, num2, operation)
			print(calc)
		
		# Catching any Value Error when a user enters a value apart from a number.
		except ValueError:
			print("Invalid number try again.")
		# Catching when a user inputs the denominator as "0".
		except ZeroDivisionError:
			print("Can not divide by zero.")
		# Catching any other exception that is identified in users inputs.
		except Exception as e:
			print(e)
		# This takes the place of exit the difference is it asks the user in a friendly way.
		if input("Do you want to continue (y/n): ") == 'n':
			break
			
if __name__ == '__main__':
	main()