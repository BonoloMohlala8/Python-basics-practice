amount_due = int(50)
while amount_due > 0:
    print("amount due: ", amount_due)

    coin = int(input("Insert Coin: "))

    if coin in [ 25, 10, 5]:
        amount_due-= coin
        print(amount_due)

change_owed = abs(amount_due)
print("\tChange owed: ", change_owed)




    
    



