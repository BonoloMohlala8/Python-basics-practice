from random import choice

lot = ["1","2","3","4","5","6","7","8","9","10","a","b","c","d","e"]
winning_ticket = []

while len(winning_ticket) <4:
    pick = choice(lot)
    if pick not in winning_ticket: 
        winning_ticket.append(pick)

print("Any ticket that matches this lot will win a prize\n")
print(f"The winning ticket: {winning_ticket}")


