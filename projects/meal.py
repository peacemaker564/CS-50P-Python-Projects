#Creating a program that accepts input from the user in 24 hours format, and tells the user whether its time to have breakfast, lunch or dinner.


def main():

    xtime = input("What time is it? ").strip()
    xtime = convert(xtime)
    if 7.0 <= xtime <= 8.00:
        print("Breakfast!")

    elif 12.0 <= xtime <= 13.00:
        print("Lunch!")

    elif 18.0 <= xtime <= 19.00:
        print("Dinner!")
    else:
        print("You are past/early your meal times.")
    ...


def convert(time):
    first, second = time.split(":")
    first = int(first)
    second = (float(second))/60
    return first+second
    ...


if __name__ == "__main__":
    main()
