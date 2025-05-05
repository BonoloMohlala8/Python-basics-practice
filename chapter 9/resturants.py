class Resturant: 


    def __init__(self,name,cuisine_type):
        self.name = name 
        self.cuisine_type = cuisine_type
        self.number_served = 0

    def describe_resturant(self):
        print(f"The resturant name is {self.name}.") 
        print(f" {self.name} offer's {self.cuisine_type} cuisine.")
    
    def open_resturant(self): 
        print(f"The resturant is now open!")
    
    def served_customers(self,served):
        if served >= self.number_served:
            self.number_served = served 
        else: 
            print("Error: Number served cannot be less than the current count.")
            print(f"This is the number of customers that have been served: {self.number_served}")





