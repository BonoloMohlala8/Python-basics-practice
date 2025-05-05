players = ['charles', 'martina', 'michael', 'florence', 'eli']

record = players[:]
players.append("Malcom")
record.append("George")

print("my fav players are: ")
for player in players:
    print(players)

print("\nHere is the first 3 picks pick of players:")
print(players[:3])

print("\nHere is the middle 3 picks pick of players:")
print(players[1:4])

print("\nHere is the last 3 picks pick of players:")
print(players[-3:])

print("\nhere is a copy of players for the record:")
for value in record:
    print(value)




