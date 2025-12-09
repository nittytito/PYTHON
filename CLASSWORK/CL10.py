from abc import ABC, abstractmethod
class User(ABC):
    def __init__(self,name,join_year):
        self.name = name
        self.join_year = join_year
    def calculate_year(self):
        current_year = 2025
        return current_year - self.join_year
  
    @abstractmethod
    def display(self):
        pass

class Customer(User):
    def __init__(self, name, joined_year):
        super().__init__(name, joined_year)
        self.role = "Customer"

    def display(self):
        print("Name: ",self.name)
        print("Role: ",self.role)
        print("Years on Platform: ",self.calculate_year())


class Vendor(User):
    def __init__(self, name, joined_year):
        super().__init__(name, joined_year)
        self.role = "Vendor"

    def display(self):
        print("Name: ", self.name)
        print("Role: ", self.role)
        print("Years on Platform: ",self.calculate_year())
customer = Customer("Miya", 2020)
vendor = Vendor("Kiran", 2018)
print("Customer")
customer.display()
print("Vendor")
vendor.display()