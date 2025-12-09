class Employee:
    def __init__(self,name,role):
        self.name = name
        self.role = role
    def display(self):
        print("Name: ",self.name)
        print("Role: ",self.role)

class Trainer(Employee):
    def __init__(self, name, specialization):
        super().__init__(name, "Trainer")
        self.specialization = specialization
    def display(self):
        super().display()
        print("Specilization:",self.specialization)

class YogaInstructor(Employee):
    def __init__(self, name, yoga_style):
        super().__init__(name, "Yoga Instructor")
        self.yoga_style = yoga_style
    def display(self):
        super().display()
        print("Yoga Style: ",self.yoga_style)

class MultiTrainer(Trainer,YogaInstructor):
    def __init__(self, name, specialization, yoga_style):
        Employee.__init__(self, name, "Multi Trainer")
        self.specialization = specialization
        self.yoga_style = yoga_style
    def display(self):
        print("Name: ",self.name)
        print("Role: ",self.role)
        print("Specialization: ",self.specialization)
        print("Yoga Style: ",self.yoga_style)

employee = Employee("Miya","Receptionist")
trainer = Trainer("Kiran", "Weight Training")
yogainstructor = YogaInstructor("Meera","Hatha Yoga")
multitrainer = MultiTrainer("Arjun","Strength Training","Power Yoga")

print("Employee")
employee.display()
print("\nTrainer")
trainer.display()
print("\nYoga Instructor")
yogainstructor.display()
print("\nMulti Trainer")
multitrainer.display()

    
    