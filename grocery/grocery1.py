items_dict = {}

while True:
    try:
        item = input("").upper()
        if item in items_dict:
            items_dict[item] += 1

        else:
            items_dict[item] = 1

    except EOFError:
        print("EOFError received, ending the program.")
        break
    else:
        continue

for i in sorted(item_dict):
    print(f"{item_dict[i]} {i}")
