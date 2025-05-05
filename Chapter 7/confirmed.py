#Key Differences from Number Increment Loop:
#With a number increment loop (number += 1), you manually control the iteration variable.
#Here, pop() automatically handles the iteration by modifying the list directly, ensuring each element is processed only once.
unconfirmed_users = ['alice','brian','candace']
confirmed_users  = []

while unconfirmed_users: 
    current_user = unconfirmed_users.pop()

    print(f"Verifying user: {current_user.title()}")
    confirmed_users.append(current_user)

print("\nThe following users have been confirmed: ")
for user in confirmed_users: 
    print(user.title())


   




