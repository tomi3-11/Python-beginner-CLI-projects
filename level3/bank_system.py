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

class BankAccount:
    def __init__(self, user, password, balance=0):
        self.user = user
        self.__password = password
        self.balance = balance
        self.is_authenticated = False


    def login(self, password):
        if password == self.__password:
            self.is_authenticated = True
            print(f"{self.user} logged in successfully!")
        else:
            print("Incorrect password!")


    def require_authentication(func):
        def wrapper(self, *args, **kwargs):
            if not self.is_authenticated:
                print("Access denied! Please log in first.")
                return
            return func(self, *args, **kwargs)
        return wrapper


    def log_transaction(func):
        def wrapper(self, *args, **kwargs):
            #print(f"Transaction: {func.__name__} called with args={args}, kwargs={kwargs}")
            return func(self, *args, **kwargs)
        return wrapper


    @require_authentication
    @log_transaction
    def deposit(self, amount):
        if amount > 0:
            self.balance += amount
            print(f"Deposited ₹{amount}. New balance: ₹{self.balance}")
        else:
            print("Invalid deposit amount!")


    @require_authentication
    @log_transaction
    def withdraw(self, amount):
        if amount <= 0:
            print("Invalid withdrawal amount!")
        elif amount > self.balance:
            print("Insufficient balance!")
        else:
            self.balance -= amount
            print(f" Withdrawn ₹{amount}. Remaining balance: ₹{self.balance}")


    @require_authentication
    @log_transaction
    def check_balance(self):
        print(f"Current balance: ₹{self.balance}")


if __name__ == "__main__":
    acc = BankAccount("Atharva", "1234", 5000)
    acc.login("1234")
    acc.check_balance()
    acc.deposit(20000)
    acc.withdraw(10000)
    acc.check_balance()