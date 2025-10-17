def main():
    n = int(input("Whats n? "))
    print_column(n)
    print_row(n)


def print_row(length):
      for i in range(length):
            print("?" )

def print_column(height):
#    for _  in range(height):
#       print("#")

#another way of writing this is print("#")
        print("#\n" * height, end = "")


main()
