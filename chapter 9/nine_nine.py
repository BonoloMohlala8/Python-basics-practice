class Car: 
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.odometer_reading = 0

    def get_descriptive_name(self):
        long_name = f"{self.year} {self.make} {self.model}"
        return long_name.title()

    def read_odometer(self):
        print(f"This car has {self.odometer_reading} miles on it.")

    def update_odometer(self, mileage):
        if mileage >= self.odometer_reading:
            self.odometer_reading = mileage
        else:
            print("You can't roll back an odometer!")

    def increment_odometer(self, miles):
        self.odometer_reading += miles

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
    
    def upgrade_battery(self):
        if self.battery_size < 65:
            self.battery_size = 65
            print(f"the new battery size is 65")
        else: 
            print("the battery is already upgraded")

class ElectricCar(Car):
    def __init__(self, make, model, year,):

        super().__init__(make, model, year)
        self.battery = Battery()



    """overriding parent class methods that arent necessary"""
    def fill_gas_tank(self): 
        print(f"This {self.make} does not have a gas tank to fill up.")

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print('\nUpgrading battery...\n')

my_leaf.battery.upgrade_battery()
my_leaf.get_descriptive_name()
my_leaf.battery.describe_battery()
my_leaf.battery.get_range()
