dinner = ["drake", "nelly", "travis"]
print("orginal list:")
print(dinner)
unnavailable = dinner.pop()
print("\n" + unnavailable + " is unnable to attend the dinner tonight \n")

dinner.insert(2, "ronaldo")
print("updated list")
print(dinner) 
print("\n")

print("A larger table has been found, therefore we will be adding 3 more guests!\n")

dinner.insert(0,"messi")
dinner.insert(2, "lebron")
dinner.append("idris")
print("Final dinner list:")
print(dinner)

for guest in dinner: 
    print("\nDear, " + guest.title() + " you are invited to my dinner party tonight!")

print(" Unfortunately we can now only accomodate for 2 guests")


removed = dinner.pop()
print( "Sorry, we could not accomodate you " + removed)
removed_1 = dinner.pop()
print( "Sorry, we could not accomodate you " + removed_1)
removed_2 = dinner.pop()
print( "Sorry, we could not accomodate you " + removed_2)
removed_3 = dinner.pop()
print( "Sorry, we could not accomodate you " + removed_3)
print(dinner)
 
for guest in dinner: 
    print("congratulations!, " + guest.title() + " You have made the final guest list. " )
del dinner[0]
del dinner[0]
print(dinner)