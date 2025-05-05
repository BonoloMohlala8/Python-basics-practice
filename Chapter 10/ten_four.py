from pathlib import Path 

name = input("Enter you first name here: ")
path = Path('guest.txt')
path.write_text(name)