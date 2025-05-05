alien = {"x_coordinates": 0, "y_coordinates": 25, "speed": "medium"}

print(f"Orginal position: {alien["x_coordinates"]}")

# Move alien to the right
# determine how far to move alien based on speed

if alien["speed"] == "slow":
    x_increment = 1
elif alien["speed"] == "medium":
    x_increment = 2
else: 
    x_increment = 3

# old position added to new increment = new position 
del alien["y_coordinates"]
new_position = alien["x_coordinates"] + x_increment

print(f"New position: {new_position}") 

