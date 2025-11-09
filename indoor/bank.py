#Bank greeting project.

owed_amount = 0;
greeting = input("What greeting did u receive? ").strip().lower()
if greeting == "hello":
    print("You are owed $", owed_amount)

elif greeting[0] == 'h':
    owed_amount = 20
    print("You are owed $", owed_amount)

else:
    owed_amount = 100
    print("You are owed $", owed_amount)



