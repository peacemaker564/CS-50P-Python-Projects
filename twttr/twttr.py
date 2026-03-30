def main():
    argument = input("Input: ").strip

    vowels = ['a', 'e', 'i', 'o' , 'u']
    string = ""

    for ch in argument:
        if not ch in vowels:
            string = string + ch


    print(f"Output: {string}")

main()
