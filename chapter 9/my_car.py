from car import Car

my_new_car = Car('Audi','RS3',2025)
print(my_new_car.get_descriptive_name())

my_new_car.update_odometer(30_000)
my_new_car.read_odometer()

my_new_car.increment_odometer(300)
my_new_car.read_odometer()

