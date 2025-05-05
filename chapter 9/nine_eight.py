class User: 

    def __init__(self,first_name,last_name,email,login = 0):
        self.first_name = first_name 
        self.last_name = last_name 
        self.email = email
        self.login = login
    
    def describe_user(self):
        print(f"\nI'm {self.first_name} {self.last_name} and this is my email {self.email}")

    def greet_user(self): 
        print(f"\nHi,{self.first_name} {self.last_name}")
    
    def increment_login_attempts(self,attempt):
        if attempt > 0:
            self.login += attempt 
        else: 
            print("The number entered has to be positive")
        print(f"these are the total number of login attempts: {self.login}")

    def reset_login_attempts(self):
        self.login = 0
        print("Login attempts have been reset to 0")

class Admin(User): 
    def __init__(self,first_name,last_name,email,login = 0):
        super().__init__(first_name,last_name,email,login) 
        self.privileges = Privileges()

class Privileges: 
    def __init__(self,privileges = []): 
        self.privileges = privileges 
    
    def show_privileges(self): 
        print(f"This is the admins list of privileges: ")
        if self.privileges:
            for privilege in self.privileges:
                print(privilege)
        else: 
            print("This user does not have privileges.") 


Bonolo = Admin('Bonolo','Mohlala','bonolomohlala8@gmail.com')


Bonolo.privileges.privileges = [
        "can add post",
        "can delete post",
        "can ban user"
]

Bonolo.privileges.show_privileges()