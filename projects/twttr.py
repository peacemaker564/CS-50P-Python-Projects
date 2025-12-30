#Writing a code that removes the vowels(a,e, i, o, u)

stringP = input("Input: ")
vowels = {'a', 'e', 'i', 'o', 'u'}
finalString = ""

for ch in stringP:
    if ch in vowels:
        continue

    else:
        finalString += ch

print("Output: ", finalString)
