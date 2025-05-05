def pet(pet_type,pet_name='sparky'): # << default value
    """Display information about a pet"""
    print(f"I have a {pet_type} ")
    print(f"My {pet_type}'s name is {pet_name.title()}")
pet("dog","Sparky")

#keyword arguments are name-value pairs in arguments (clears up order)
#for example:

pet(pet_type="cat",pet_name="sissy")