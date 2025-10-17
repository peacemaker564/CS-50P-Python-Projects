def main():
    n = int(input("Whats n? "))
    print_column(n)

def print_column(height):
#    for _  in range(height):
#       print("#")

#another way of writing this is print("#")
        print("#\n" * height, end = "")

main()
