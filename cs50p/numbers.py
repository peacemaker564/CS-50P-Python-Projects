def main():
    z = getint("What is z? ")
    print(f"z is {z}")

def getint(prompt):

    while True:
        try:
            return int(input(prompt))
            #instead of return int, we can also return x, after x = int(input("..."))
        except ValueError:
            pass
            #print("x is not an integer.!")

        #else:
            #return x; //could be this way, or the other.

main()

