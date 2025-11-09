#Bank greeting project.

def main():
    greet = input("What greeting did u receive? ").strip().lower()
    x = greeting(greet)
    print("You are owed $" , x)

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

main()

