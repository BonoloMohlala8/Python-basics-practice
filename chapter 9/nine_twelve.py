from Admin_privileges import Admin, Privileges
Drake = Admin("Aubery","Graham","Auberygraham@gmail.com")

Drake.privileges.privileges = [
    "can post",
    "can delete post", 
    "can edit post",
]

Drake.privileges.show_privileges()