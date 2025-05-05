# Write a program that polls users about their dream vacation. 

dream_vacation = {}
# Write a prompt similar to If you could visit one place in the world, where would you go?

poll_active = True

while poll_active:
    name = input("Enter your name: ")
    response = input("if you could visit one place in the world, where would you go ? ")
    dream_vacation[name] = response

    repeat = input("Do you want to submit another reponse? ") 
    if repeat == 'no':
        poll_active = False

# Include a block of code that prints the results of the poll.

print("\n--- Poll results ---")
for name,response in dream_vacation.items():
    print(f"Congrats,{name}!. \n You have been selected to go to {response} for a 3 week vacation!\n")
