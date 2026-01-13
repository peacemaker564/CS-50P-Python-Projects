def main():
    plate = input("Plate: ")
    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if not(2 <= len(s) <= 6): #requirement 1 complete. range confirmed.
        return False

    if not s.isalnum(): # requirement 2 complete. alphabet or either number confirmed.
        return False

    if not (s[0].isalpha() and s[1].isalpha()): #requirement 3 complete. First and second values of the user input confirmed as alphabets.
        return False

    number_started = False #boolean variable for number_starting scenario to further check the other requirements.
    for ch in s[2:]:
        if ch.isdigit(): #checks if the 3rd value is a digit or not, and if its 0, return false.

            if not number_started:

                if ch == "0":
                    return False
                number_started = True

        else: #if its not a digit, and alphabet, return false.
            if number_started:
                return False

    return True

main()
