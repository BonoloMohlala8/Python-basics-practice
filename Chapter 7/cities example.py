prompt = "\nEnter the name of the city you have visted:"
prompt += "\n(Enter'quit' when you are finished)"

while True: 
    city = input(prompt)
    if city == 'quit':
        break 
    else:
        print(f"I'd like to go to {city.title()}!")
