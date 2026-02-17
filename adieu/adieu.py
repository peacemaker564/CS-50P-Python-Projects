#Instructions:
#In a file called adieu.py, implement a program that prompts
# the user for names, one per line, until the
# user inputs control-d. Assume that the user
# will input at least one name.
# Then bid adieu to those names, separating two names with one and,
# three names with two commas and one and,
# and 𝑛 names with 𝑛 −1 commas and one and, as in the below:

def main():
    name_list = []
    while True:
         try:
             name_list.append(input("Name: "))

         except EOFError:
            print("End of input detected.")
            break

    print("Adieu, Adieu to", end ="")

    for i in name_list:

        if i == name_list[-1]:
            print(",and ", i)
        else:
            print(i,"," end = "")



main()



