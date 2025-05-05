def greet_users(names):
    for name in names:
        message = f"Hello, {name.title()}!"
        print(message)

users = ['hannah','bonolo','john'] 
greet_users(users)