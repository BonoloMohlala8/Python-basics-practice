def make_sandwich(*toppings):
    print("Make a sandwich with the following toppings: ")
    for topping in toppings:
        print(f"- {topping}")
make_sandwich("chicken","lettuce")
make_sandwich("beef","tomato","guac")
make_sandwich("ham","cheese")