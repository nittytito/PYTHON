class account:
    def __init__(self,name,balance):
        self.name = name
        self.balance = balance
    def __add__(self, other):
        return self.balance + other.balance
class SavingsAccount(account):
    def calculate_interest(self):
        return self.balance * 0.05
class CurrentAccount(account):
    def calculate_interest(self):
        return self.balance * 0.02
savings = SavingsAccount("Ravi",10000)
current = CurrentAccount("Anjali",15000)
print("Account Details")
print("Name: ",savings.name)
print("Balance: ",savings.balance)
print("Interest: ",savings.calculate_interest())

print("Name: ",current.name)
print("Balance: ",current.balance)
print("Interest: ",current.calculate_interest())

total_balance = savings + current
print("Total Balance: ",total_balance)