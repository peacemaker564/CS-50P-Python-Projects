#This program takes the user grocery list, and output it out with the number of times it was entered in the input buffer.
#Capitalize the input, and make sure it gets printed out in alphabetical order.

import sys
items = []

count = 0

for i in range(len(sys.argv) - 1):
    item = input("")
    items.append(item).upper()

    if item in items:
        count = count+1

        for i in items:
            print(count,i)

    else:
        continue













