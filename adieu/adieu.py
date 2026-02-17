#Instructions:
#In a file called adieu.py, implement a program that prompts
# the user for names, one per line, until the
# user inputs control-d. Assume that the user
# will input at least one name.
# Then bid adieu to those names, separating two names with one and,
# three names with two commas and one and,
# and 𝑛 names with 𝑛 −1 commas and one and, as in the below:

def main():
    name_dictionary = {}
    while True:
         try:
             name = input("Name:")

             if name in name_dictionary:
                 name_dictionary[name] += 1

             else:
                 name_dictionary[name] = 1


         except EOFError:
            print("End of input detected.")
            break

    print("Adieu, Adieu to", end ="")
    for i in name_dictionary:

        if i = len(name_dictionary) - 1:
            
        print(i,"," end = "")



main()



