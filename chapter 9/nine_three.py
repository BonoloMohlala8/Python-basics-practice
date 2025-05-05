class User: 

    def __init__(self,first_name,last_name,email):
        self.first_name = first_name 
        self.last_name = last_name 
        self.email = email 

    def describe_user(self):
        print(f"\nI'm {self.first_name} {self.last_name} and this is my email {self.email}")

    def greet_user(self): 
        print(f"\nHi,{self.first_name} {self.last_name}")

user1 = User('Bonolo','Mohlala','bonolomohlala8@gmail.com')
user2 = User('Aubery', 'Graham','drakeovo@icloud.com')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()
