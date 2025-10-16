def main():
    number = get_number()
    meow(number)

def get_number():
    while True:
        n = int(input("What the value of n? "))
        if n > 0:
            return n #This will automatically break out of the loop.

def meow(n):
    for _ in range(n):
        print("meow")

main()
