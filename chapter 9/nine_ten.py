from resturants import Resturant

resturant = Resturant('Nobu',"Asian")
resturant.served_customers(21)
print(f"This resturant has served {resturant.number_served} customers.")
print(f"{resturant.name} has the best {resturant.cuisine_type} cuisine")
resturant.describe_resturant()
resturant.open_resturant()
