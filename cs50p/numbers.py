def main():
    x = getint()
    print(f"x is {x}")

def getint():

    while True:

        try:
            x = int(input("What's the x? "))
        except ValueError:
            print("x is not an integer, dumbass.! Try again.")
        else:
            return x


main()

