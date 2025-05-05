class Restaurant: 


    def __init__(self,name,cuisine_type):
        self.name = name 
        self.cuisine_type = cuisine_type

    def describe_restaurant(self):
        print(f"The resturant name is {self.name}.") 
        print(f" {self.name} offers {self.cuisine_type} cuisine.")
    
    def open_restaurant(self): 
        print(f"The resturant is now open!")
    

restaurant = Restaurant('Nobu',"Asian")

print(f"{restaurant.name} has the best {restaurant.cuisine_type} cuisine")
restaurant.describe_restaurant()
restaurant.open_restaurant()


class IceCreamStand(Restaurant): 
    def __init__(self,name,cuisine_type,flavours = None):
        super().__init__(name,cuisine_type )
        if flavours is None:
            self.flavours = ["Vanilla","Chocolate","Caramel"]
        else: 
            self.flavours = flavours 
             
    def ice_cream_flavours(self):
        print(f"{self.name} serves these flavours: {self.flavours}")

hometown = IceCreamStand('Milky Lane','deserts','chocolate')
