class Resturant: 


    def __init__(self,name,cuisine_type):
        self.name = name 
        self.cuisine_type = cuisine_type

    def describe_resturant(self):
        print(f"The resturant name is {self.name}.") 
        print(f" {self.name} offer's {self.cuisine_type} cuisine.")
    
    def open_resturant(self): 
        print(f"The resturant is now open!")
    

resturant = Resturant('Nobu',"Asian")

print(f"{resturant.name} has the best {resturant.cuisine_type} cuisine")
resturant.describe_resturant()
resturant.open_resturant()

        