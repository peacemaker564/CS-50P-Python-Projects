def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):

    #if not(2 <= len(s) <= 6):
    #   return False

    if not s.isalnum():
        return False

    if not(s[0].isalpha() and s[1].isalpha()):
        return False

    number_started = False
    for ch in s[2:]:
        if ch.isdigit:
            if not number_started:
                if ch == 0:
                    return false
                number_started = True

        else:
            if number_started:
                return False #As cannot go back to alphabets, once number starts.


    return True



if __name__ == "__main__":
    main()


