def main():
    argument = input("Input: ").strip()
    print(F"Output: {shorten(argument)}")


def shorten(word):

    vowels = ['a', 'e', 'i', 'o' , 'u']
    string = ""
clear
    for ch in word:
        if not ch.lower() in vowels:
            string = string + ch


    return string

if __name__ == "__main__":
    main()
