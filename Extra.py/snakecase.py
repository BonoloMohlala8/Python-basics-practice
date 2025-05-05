# get user input 

camelcase = input("CamelCase: ")

# print "snake case: ""

print("Snakecase: ", end = "")

# loop through every letter 

for letter in camelcase:

# check if letter is upper case
    if letter.isupper():

# print underscores and letters in lowercase 
        print("_" + letter.lower(), end = "")

# otherwise, print letter 
    else:
        print(letter, end = "")
# print space in the end 
print()
