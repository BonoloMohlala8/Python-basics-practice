class Dog: 
    '''A simple attempt to model a dog'''

    def __init__(self,name,age):
        '''Intitalize name and age attributes'''
        self.name = name 
        self.age = age 

    def sit(self):
        '''Simulating a dog sitting in response to a command.'''
        print(f"{self.name} is now sitting")

    def roll_over(self):
        '''Simulate rolling over in response to a command.'''
        print(f"{self.name} rolled over!")

my_dog = Dog('Willie',6)
her_dog = Dog('Sparky',2)

print(f"My dog's name is {my_dog.name}.")
print(f"My dog is {my_dog.age} years old.")
my_dog.sit()


print(f"\nHer dog's name is {her_dog.name}.")
print(f"her dog's age is {her_dog.age} years old.")
her_dog.sit()
