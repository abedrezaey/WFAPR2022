
class User():
	accounts = {}
	def __init__(self , name):
		self.name = name
		User.accounts[self.name] = 0
		

	
	def deposit(self, amount):
		User.accounts[self.name] += amount
		print(f"Users Checking Accounts {amount}")

	

	def withdraw(self, amount):
		User.accounts[self.name] -= amount
		print(f"User Withdraw {amount}")

	# def display_acount_info(self, balance):
	# 	self.balance = balance



user01 = User ("Jone Doe")
user02 = User ("Jone Max")


user01.deposit(1100)
user02.deposit(3000)

print(User.accounts)