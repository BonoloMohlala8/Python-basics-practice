from electric_car import ElectricCar

my_leaf = ElectricCar('nissan', 'leaf', 2024)
print(my_leaf.get_descriptive_name())

my_leaf.battery.describe_battery()
my_leaf.battery.get_range()

#'''the comment below is to import an entire module'''
#import car module 
#my_new_car = car.Car('Audi','RS3',2025)
#my_leaf = car.ElectricCar('nissan,'leaf', 2024)