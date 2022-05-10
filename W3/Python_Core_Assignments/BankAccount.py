class BankAccount (): 
	accounts = {}

	def __init__(self, int_rate = 0.01, balance = 0): 
		self.int_rate = int_rate
		
		self.balance = balance
		BankAccount.accounts[self.balance] = 0

	def deposit(self, amount): 
		BankAccount.accounts[self.balance] += amount
		print(f"Amount Deposited {amount}")
		return self.balance



	def withdraw(self, amount):
		# BankAccount.accounts[self.balance] -= amount
		if self.balance < 0 :
			print("Insufficient funds: Charging a $5 fee")
		self.balance = self.balance - amount
		return self.balance


	def display_account_info(self):
		print(f"Balance: {self.balance}")


	def yield_interest(self):
		if self.balance > 0 :
			self.balance += self.balance * self.int_rate
		
			print("Yield")
		return self.int_rate and self.balance


account1 = BankAccount("Deposits")
account2 = BankAccount("Deposits")
account1.display_account_info()
account1.yield_interest()

account1.deposit(50)
account1.deposit(60)
account1.deposit(70)
account1.withdraw(80)

account2.deposit(10)
account2.deposit(5)
account2.withdraw(20)
account2.withdraw(25)
account2.withdraw(30)
account2.withdraw(35)


print(BankAccount.accounts)