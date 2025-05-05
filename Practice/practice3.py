toppings = ["mushrooms","onions","pineapple"]
glucose = "bread"
if glucose not in toppings: 
    print(f"{glucose.title()}, You cannot choose this topping for you meal")

car = "bmw"
print("does car == bmw? i predict true")
print(car == "bmw")
print("does car == mercedes ? i predict false")
print(car == "mercedes")
age = 14
print(age == 15)
print(age >= 10)
print(age <= 20)

soccer = ["man city", "man united", "arsenal", "liverpool"]
team = "Man city"
if team.lower() in soccer:
    print(f"{team}, is in the list")
else: 
    print(f"{team}, is not the list")
