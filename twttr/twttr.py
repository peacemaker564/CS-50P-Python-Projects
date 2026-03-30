def main():
    argument = input("Input: ").strip()
    print(F"Output: {shorten(argument)}")


def shorten(word):

    vowels = ['a', 'e', 'i', 'o' , 'u']

    for ch in word:
        if not ch.lower() in vowels:
            string = string + ch


    return string

main()
