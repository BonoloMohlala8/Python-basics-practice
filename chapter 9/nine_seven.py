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
        self.privileges = ["can delete post", "can add post", "can ban user"]

    def show_privileges(self): 
        print(f"This is the admins list of privileges: {self.privileges}")
        

admin = Admin('someone','else','me@me.com')
user1 = User('Bonolo','Mohlala','bonolomohlala8@gmail.com')
user2 = User('Aubery', 'Graham','drakeovo@icloud.com')

user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()
user1.increment_login_attempts(2)
user2.increment_login_attempts(4)
user1.reset_login_attempts()
admin.show_privileges()