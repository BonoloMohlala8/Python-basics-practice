while True:
    num1 = input("Enter the first number:")
    if num1 == 'q':
        break

    num2 = input("Enter the second number:")
    if num2 =='q':
        break

    try: 
        added = int(num1) + int(num2)
        print(f"the answer is {added}")
    except ValueError:
        print("Oops!, you need to enter valid numbers only")
    
         