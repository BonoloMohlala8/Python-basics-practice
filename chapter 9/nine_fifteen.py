from random import choice

lot = ["1","2","3","4","5","6","7","8","9","10","a","b","c","d","e"]


def generate_ticket(lot):
    ticket = []
    while len(ticket) <4:
        pick = choice(lot)
        if pick not in ticket: 
            ticket.append(pick)
    return ticket
winning_ticket = generate_ticket(lot)


print("Any ticket that matches this lot will win a prize\n")
print(f"The winning ticket: {winning_ticket}")


my_ticket = ['e','7','6','3']
attempts = 0 
won = False 
max_attempts = 1_000_000


while not won and attempts < max_attempts:
    new_ticket = generate_ticket(lot)
    attempts += 1 

    if sorted(new_ticket) == sorted(my_ticket):
        won = True 
        print(f"\nit took {attempts} to get your ticket")
        print(f"Your ticket: {my_ticket}")
        print(f"Winning_ticket{new_ticket}")
if not won: 
        print("\nYour ticket did not win")
        



