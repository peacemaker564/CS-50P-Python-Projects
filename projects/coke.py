#This program asks the user for amount(cost) of a Coke, which costs 50 cents. The machine only accepts 25, 10 and 5
#cents, every once. When the user enters the amount, pass them the amount due, and if paid more, the amount owed.


VALID_COINS = {10, 25, 50}
amount_due = 50

while amount_due > 0:

        amount_entered = int(input("Enter a coin: "))
        if amount_entered not in VALID_COINTS:
                print("Not accepted. Please Enter another coin: ")
                continue

        amount_due = amount_due - amount_entered

