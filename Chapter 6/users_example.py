users = {
 'aeinstein': {
 'first': 'albert',
 'last': 'einstein',
 'location': 'princeton',
 },
 'mcurie': {
 'first': 'marie',
 'last': 'curie',
 'location': 'paris',
 },
 }

for username, user_info in users.items():
    print(f"Username: {username}")
    names = f"{user_info['first']} {user_info['last']}"
    location = user_info['location']
    print(f"\tFull name:{names}")
    print(f"\tlocation:{location}")



