class vehicle:
    def __init__(self,vehicle_id,base_rate):
        self.vehicle_id = vehicle_id
        self.base_rate = base_rate
    def display_details(self):
        return f"Vehicle ID: {self.vehicle_id}, Base Rate: {self.base_rate}"
    def rental_charge(self):
        return 0.0        

class car(vehicle):
    def __init__(self, vehicle_id, base_rate,num_seats):
        super().__init__(vehicle_id, base_rate)
        self.num_seats = num_seats
    def rental_charge(self):
        return self.base_rate * self.num_seats
    
class bike(vehicle):
    def __init__(self, vehicle_id, base_rate,bike_type):
        super().__init__(vehicle_id, base_rate)
        self.bike_type = bike_type
    def rental_charge(self):
        return self.base_rate * 0.5
def calculate_rental(vehicle):
    return vehicle.rental_charge()
car1 = car("CAR001",100.0,4)
bike1 = bike("BIKE001",50.0,"SCOOTER")
print(car1.display_details())
print(bike1.display_details1())
print("Car rental charge: ",calculate_rental(car1))
print("Bike rental charge: ",calculate_rental(bike1))