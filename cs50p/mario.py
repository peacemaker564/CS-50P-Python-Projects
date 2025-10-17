def main():
    rows = int(input("Whats n? "))
    col = int(input("Whats m? "))
    print_rowcol(col, rows)


def print_rowcol(height, length):
        for i in range(height):
            print("?" * length)


main()
