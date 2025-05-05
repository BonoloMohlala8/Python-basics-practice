# Using the list sandwich_orders from Exercise 7-8, make sure the sandwich 'pastrami' appears in the list at least three times. 
sandwich_orders = ['pastrami','chicken mayo','pastrami','cheese','vegan','pastrami','tuna']

# Add code near the beginning of your program to print a message saying the deli has run out of pastrami
print("The deli has run out of pastrami")
# and then use a while loop to remove all occurrences of 'pastrami' from sandwich_orders.

while 'pastrami' in sandwich_orders:
     sandwich_orders.remove('pastrami')
#Make sure no pastrami sandwiches end up in finished_sandwiches.
print(sandwich_orders)