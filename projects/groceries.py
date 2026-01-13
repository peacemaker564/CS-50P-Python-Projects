#Writing a program that collects the user's grocery list
#and outputs the number of times the item was repeated and also listed alphabetically.

grocery_list = []

while True:

    try:
        grocery_item =  input("item: ").upper()
        grocery_list.append(grocery_item)

    except EOFError:
        print("EOR Detected.")
        break


print("\n")

for item in grocery_list:
            print(item)


# Step1: Successful printing.
# Steps left 2. to execute. Sorting in alphabetical order.
# 3. checking elements for repetition and mentioning the number of times they were repeated.





