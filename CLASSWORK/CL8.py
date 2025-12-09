class Person:
    def __init__(self,name,age):
        self.name = name
        self.age = age
    def show_details(self):
        print("Name: ",self.name)
        print("Age: ",self.age)

class Employee(Person):
    def __init__(self, name, age,employee_id):
        Person.__init__(self,name, age)
        self.employee_id = employee_id
    def show_details(self):
        Person.show_details(self)
        print("Employee ID: ",self.employee_id)

class PartTime(Person):
    def __init__(self, name, age,working_hours):
        Person.__init__(self,name, age)
        self.working_hours = working_hours
    def show_details(self):
        Person.show_details(self)
        print("Working Hours: ",self.working_hours)

class Consultant(Employee, PartTime):
    def __init__(self, name, age, employee_id, working_hours, project_name):
        Employee.__init__(self,name,age,employee_id)
        PartTime.__init__(self,name,age,working_hours)
        self.project_name = project_name
    def show_details(self):
        Employee.show_details(self)
        print("Working Hours: ",self.working_hours)
        print("Project_Name: ",self.project_name)

person1 = Person("Miya",22)
employee1 = Employee("Meenu",30,"EMP101")
parttime1 = PartTime("Liya",26,4.5)
consultant1 = Consultant("Amiya",28,"EMP202",5.0,"FULL STACK")

print("\n PERSON DETAILS")
person1.show_details()
print("\n EMPLOYEE DETAILS")
employee1.show_details()
print("\n PART TIME DETAILS")
parttime1.show_details()
print("\n CONSULTANT DETAILS")
consultant1.show_details()