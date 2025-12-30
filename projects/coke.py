#This program asks the user for amount(cost) of a Coke, which costs 50 cents. The machine only accepts 25, 10 and 5
#cents, every once. When the user enters the amount, pass them the amount due, and if paid more, the amount owed.


VALID_COINS = {10, 25, 5}
amount_due = 50

while amount_due > 0:

        print("Amount due:", amount_due) ;

        amount_entered = int(input("Enter a coin: "))
        if amount_entered not in VALID_COINS:
                print("Not accepted. Please Enter another coin: ")
                continue #if coin_entered is not valid, keeps repeating until right coin entered.

        amount_due = amount_due - amount_entered #tracks ammount_due

if amount_due < 0:
        print("Chang owed is:", abs(amount_due)) # prints the amount owed to the user ignoring the negative sign.
else:
        print("Changed owed is:", amount_due) #print 0.
