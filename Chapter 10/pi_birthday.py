from pathlib import Path

path = Path("pi_million_digits.txt")
contents = path.read_text()

pi_string = ''

for line in contents.splitlines(): 
    pi_string += line.strip()

birthday = input("Enter your birthday, use MM/DD/YY fromating: ")
if birthday in contents: 
    print("you birthday is in the firt million digits of pi!")
else: 
    print("Your birthday is not in the first million digits of pi")