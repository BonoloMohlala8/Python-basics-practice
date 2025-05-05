responses = {}
#Set a flag to indicate that polling is active.
poll_active = True

# Prompt for the person's name and response.
while poll_active: 
    name = input("What is your name? ")
    response = input("Which mountain are you interested in climbing? ")

# Store the response in the dictionary.
    responses[name] = response
# Find out if anyone else is going to take the poll.
    repeat = input("Enter [yes/no] if you want another person to poll: ")
    if repeat.lower() == 'no':
        poll_active = False  
# Polling is complete. Show the results.
print("\n--- Poll results ---")
for name,response in responses.items():
    print(f"{name} would like to climb {response}.")