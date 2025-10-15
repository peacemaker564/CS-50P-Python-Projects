#Program to check even or odd values.
def main():
    x = int(input("Whats x? "))

    if evenOdd(x):
        print("The number is even")
    else:
        print("Its odd.")

def evenOdd(num):
    return True if num % 2 == 0 else False


main()
