prompt = "Enter your first name? "

while True:
    name = input(prompt)
    
    if name.lower() == "quit":
        break

    if len(name.split()) > 1:
        print("try again") 
    else:
        print(f"Hi,{name.title()}")