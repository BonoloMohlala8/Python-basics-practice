# Make a list called sandwich_orders and fill it with the names of various sandwiches
sandwich_orders = ['chicken mayo','cheese','vegan','tuna']

# Then make an empty list called finished_sandwiches.
finished_sandwiches = []

# Loop through the list of sandwich orders and print a message for each order, such as I made your tuna sandwich.
for sandwich in sandwich_orders:
        print(f"I made your {sandwich} order.")

# As each sandwich is made, move it to the list of finished sandwiches
while sandwich_orders:
        sandwiches = sandwich_orders.pop()
        finished_sandwiches.append(sandwiches)

        
#. After all the sandwiches have been made, print a message listing each sandwich that was made.
for finished_sandwich in finished_sandwiches:
        print(f"Your {finished_sandwich} is ready for collection")
