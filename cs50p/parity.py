#Program to check even or odd values.
def main():
    x = int(input("Whats x? "))
    evenOdd(x)

def evenOdd(num):
    if num % 2 == 0:
        print("The number is even.")
    else:
        print("The entered number is odd.")


main()
