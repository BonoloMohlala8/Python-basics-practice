from pathlib import Path 

path = Path('guest_book.txt')

print("Enter 'q' to quit the program" "\nEnter 2 numbers an i'll add them up for you")

while True: 

    numbers = input('Enter your first number here:')
    if numbers.lower() == 'q':
        break

    numbers2 = input("Enter your second number here:")
    if numbers2.lower() == 'q': 
        break
    try:
        addition = int(numbers) + int(numbers2)
    except ValueError:
        print("oops, looks like you've entered text instead of a number")
    else:
        with path.open(mode = 'a') as file:
            file.write(f"{numbers} + {numbers2} = {addition}\n")
        print(f"Your answer is {addition}")

