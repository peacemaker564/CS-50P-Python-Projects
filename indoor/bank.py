#Bank greeting project.


greet = input("What greeting did u receive? ").strip().lower()
print("You are owed " , greeting(greet))

def greeting(greet):
    if greet == "hello":
        owed_amount = 0
        return owed_amount

    elif greet[0] == 'h':
        owed_amount = 20
        return owed_amount
    else:
        owed_amount = 100
        return owed_amount



