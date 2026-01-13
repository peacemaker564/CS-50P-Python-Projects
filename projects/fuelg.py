while True:
    try:
        fraction = input("Fraction: ")
        x, y = fraction.split("/")
        x = int(x)
        y = int(y)
        div = int((x/y)*100)

    except ValueError:
        print("Please enter appropriate values. ")
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
            print(div,"%", sep = "")

    break









