from calculator import square

def main():
    test_square()

def test_square():
    if square(2) != 4:
        print("incorrect value of square 2.")

    if square(3) != 9:
        print("incorrect value of square 3.")

if __name__ == "__main__":
    main()
