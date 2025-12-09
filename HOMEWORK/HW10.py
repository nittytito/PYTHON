from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self, name, account_year):
        self.name = name
        self.account_year = account_year
    def account_age(self):
        current_year = 2025
        return current_year - self.account_year
    
    @abstractmethod
    def get_role(self):
        pass

class Admin(User):
    def get_role(self):
        return "Admin"
    def __str__(self):
        return f"Admin User: {self.name }, Account Age: {self.account_age()}"

class Guest(User):
    def get_role(self):
        return "Guest"
    def __str__(self):
        return f"Guest User: {self.name} , Account Age: {self.account_age()}"

adminuser= Admin("Miya",2020)
guestuser = Guest("Kiran",2023)

print("Admin User")
print("Admin Role:",adminuser.get_role())
print("Admin Account Age: ",adminuser.account_age())
print(adminuser)

print("Guest User")
print("Guest Role:",guestuser.get_role())
print("Guest Account Age: ",guestuser.account_age())
print(guestuser)