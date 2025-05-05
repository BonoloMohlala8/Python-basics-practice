"""A class that can be used as to respresent a car"""

class Car: 

    def __init__(self,make,model,year): 
        self.make = make
        self.model = model 
        self.year = year 
        self.odometer_reader = 0
    
    def get_descriptive_name(self): 
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()
    
    def update_odometer(self,mileage):
        if mileage >= self.odometer_reader:
            self.odometer_reader = mileage
        else: 
            print("You cannot roll back")
    
    def read_odometer(self):
        print(f"This car has {self.odometer_reader} kilometres on it.") 

    def increment_odometer(self,miles): 
        self.odometer_reader += miles

