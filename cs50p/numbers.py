def main():
    x = getint()
    print(f"x is {x}")

def getint():

    while True:
        try:
            return int(input("Whats x? "))
            #instead of return int, we can also return x, after x = int(input("..."))
        except ValueError:
            pass
            #print("x is not an integer.!")

        #else:
            #return x; //could be this way, or the other.

main()

