from random import randint

class Die: 
    def __init__(self,sides = 6):
        self.sides = sides 

    def roll_die(self): 
        print(randint(1,self.sides))


roller_1 = Die(6)
roller_2 = Die(10)
roller_3 = Die(20)

print("\nNow it's roller 1's turn:")
for side in range(3): 
    roller_1.roll_die()

print("\nNow it's roller 2's turn:")       
for side in range(10):
    roller_2.roll_die()

print("\nNow it's roller 3's turn:")
for side in range(10):
    roller_3.roll_die()


    

