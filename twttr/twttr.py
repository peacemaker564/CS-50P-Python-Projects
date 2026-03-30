def main():
    argument = input("Input: ").strip
    argument = argument.lower()

    vowels = ['a', 'e', 'i', 'o' , 'u']
    string = ""

    for ch in argument:
        if not ch in vowels:
            string = string + ch


    print(f"Output: {argument}")

main()
