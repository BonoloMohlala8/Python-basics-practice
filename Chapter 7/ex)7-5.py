prompt  = "What is your age? "


while True: 
    age = input(prompt)
    if age.lower() == 'quit':
        break 
    age = int(age) 
   
    if age <= 3:
        print("Your ticket is free!")
    elif age > 3 > 12:
        print("your ticket is $10")
    else: 
        print("your ticket is $15")


    


    