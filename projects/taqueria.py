#Writing a program to accept cusstomer order, and display the price after each order, and finally the total price at the end.

menu = {
    "Baja Taco": 4.25,
    "Burrito": 7.50,
    "Bowl": 8.50,
    "Nachos": 11.00,
    "Quesadilla": 8.50,
    "Super Burrito": 8.50,
    "Super Quesadilla": 9.50,
    "Taco": 3.00,
    "Tortilla Salad": 8.00
}

price = 0

while True:

    try:
        item = input("Item: ").title()
        if item not in menu:
            continue
        price += (menu[item])
    except EOFError:
        print("EOF Error received..exiting program.")
        break
    else:
        print(f"Total: ${price:.2f}")


print(f"Final Total: ${price:.2f}")




