def main():


def
while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)

        # Check if X is greater than Y (optional, but standard for this CS50 problem)
        if x > y:
            continue

        div = round((x / y) * 100)

    except ValueError:
        print("Please enter appropriate values.")
        continue
    except ZeroDivisionError:
        print("Unethical fraction. Try again.")
        continue
    else:
        if div <= 1:
            print("E")
        elif div >= 99:
            print("F")
        else:
            print(f"{div}%")

        break
    
def convert(fraction):
    ...


def gauge(percentage):
    ...


if __name__ == "__main__":
    main()
