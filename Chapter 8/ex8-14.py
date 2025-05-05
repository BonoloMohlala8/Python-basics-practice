def build_car(manufacturer,model, **car_features):
    car_features['car_name'] = manufacturer
    car_features['model_name'] = model
    return car_features

car = build_car('BMW', 'M3', color = 'black', tow_package = True)
car2 = build_car('Mercedes', 'c63', color = 'black', tow_package = False)

print(car)
print(car2)