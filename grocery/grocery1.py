items_list = []

while true:
    try:
        item = input("").upper()

        items_list.append(item)
        if item in items_list:
            count = count + 1

    except EOFError:
        print("Exiting program.")

    else:
        for i in items_list:
            print(count, )






