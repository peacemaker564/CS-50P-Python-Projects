def main():
    argument = input("Input: ").strip
    new_arg = argument.lower()

    vowels = ['a', 'e', 'i', 'o' , 'u']
    string = ""

    for ch in new_arg:
        if not ch in vowels:
            string = string + ch


    print(f"Output: {string}")

main()
