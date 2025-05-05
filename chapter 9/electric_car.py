""" A set of class that can be used to represent electric cars """

from car import Car

class Battery: 
    def __init__(self,battery_size = 40):
        self.battery_size = battery_size
        
    def describe_battery(self):
        print(f"this car has a battery size of {self.battery_size} KWh")
    
    def get_range(self): 
        if self.battery_size == 40: 
            range = 150
        elif self.battery_size == 65:
            range = 225
        print(f"This car can travel {range} km when fully charged")

class ElectricCar(Car):
    def __init__(self, make, model, year,):

        super().__init__(make, model, year)
        self.battery = Battery()

    

    """overriding parent class methods that arent necessary"""
    def fill_gas_tank(self): 
        print(f"This {self.make} does not have a gas tank to fill up.")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

my_leaf.battery.describe_battery()
my_leaf.battery.get_range()