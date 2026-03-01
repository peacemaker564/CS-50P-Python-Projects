#Instructions:
#In a file called adieu.py, implement a program that prompts
# the user for names, one per line, until the
# user inputs control-d. Assume that the user
# will input at least one name.
# Then bid adieu to those names, separating two names with one and,
# three names with two commas and one and,
# and 𝑛 names with 𝑛 −1 commas and one and, as in the below:

# This part is to correctly append names to the list.
def main():
    name_list = []
    while True:
         try:
             name_list.append(input("Name: "))

         except EOFError:
            break

    print("\n")
    print("Adieu, Adieu, to ", end ="")

# ...

# This part is to print the names, correctly,
# on three different basis, 1. One name, 2. Two names, and
# 3. 3 or more names.
    if len(name_list) == 1:
        print(name_list[0])
    elif len(name_list) == 2:
        print(name_list[0], "and" , name_list[1])

    else:
        for i in name_list:
            if name_list[-1]:
                print("and")
            print(i, ", ")


#
main()



