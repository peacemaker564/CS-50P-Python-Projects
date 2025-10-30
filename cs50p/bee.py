words = {"HAIR": 4, "PAIR" : 4, "CHAIR" : 5, "GRAPHIC": 7}

def main():
    print("Welcome to Spelling Bee!")

    for word, points in words.items():
        print(f"{word} is worth {points} points.")

main()
