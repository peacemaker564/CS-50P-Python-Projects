def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not (2 <= len(s) <= 6):
        return False

    if not s.isalnum():
        return False

    if not (s[0].isalpha() and s[1].isalpha()):
        return False

    number_started = False
    for ch in s[2:]: #cuz we checked the first two characters already.
        if ch.isdigit():
            if not number_started:

                if ch == "0":
                    return False
                number_started = True

        else:
            #if number starts, we cannot go back to alphabets.
            if number_started:
                return False

    return True

main()
