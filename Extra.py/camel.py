# step 1: define a function that converts camel case into snake case 
# step 2: convert all first letters into lower case and add underscores.
# step 3: create variables for both inputs 
# step 4: print.

def convert(camel_case):    
    snake_case = "_"
    for i in camel_case:
        if camel_case.isupper():
             snake_case = snake_case + i.lower()
        
        else: 
                snake_case = snake_case + " " + i.lower()
    return snake_case


camel_case_name = input("Enter camel case variable:")

print("enter snake case variable: ", convert(camel_case_name))




