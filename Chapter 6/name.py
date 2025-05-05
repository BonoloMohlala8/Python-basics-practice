fav_lang = {
 'jen':'python',
 'sarah':'c',
 'edward':'rust',
 'phil':'python',
 }
users = ['jen', 'edward', 'john']
for name in users:
    if name in fav_lang:
        print(f"Hey {name}, Thanks for taking the poll")
    else:
        print(f"{name}, please take the poll.")
