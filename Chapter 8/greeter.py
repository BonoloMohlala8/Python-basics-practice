def greet_user(first,last): 
    """return a full name, neatly formatted""" 
    full_name = f"{first} {last}"
    return full_name.title()

while True:
    print("\nPlease tell me your name")
    print("press 'q' at any time to quit")

    f_name = input("First name: ")
    if f_name.lower() == "q":
        break

    l_name = input("Last name: ")
    if l_name.lower() == "q":
        break

    formatted_name = greet_user(f_name,l_name)
    print(f"\nHello,{formatted_name}")

#line 2 is a docstring, it describes what a fuction does. 



