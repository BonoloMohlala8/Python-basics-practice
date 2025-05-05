from User2 import User
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