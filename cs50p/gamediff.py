#A new program to recommend game on the basis of few conditionals.

def main():

    difficulty = input("Difficult or Casual?: ")
    if not (difficulty == "Difficult" or difficulty == "Casual"):
        print("Please enter valid difficulty.")
        return # program ends.

    player = input("Multiplayer or Single-Player?: ")

    if not (player == "Multiplayer" or player == "Single-Player"):
        print("Please enter valid player num.")
        return # program ends.

    if difficulty == "Difficult" and player == "Multiplayer" :
        recommend("Poker")

    elif difficulty == "Difficult" and player == "Single-Player" :
        recommend("Klondike")

    elif difficulty == "Casual" and player == "Multiplayer" :
        recommend("Hearts")

    else:
        recommend("Clock")


def recommend(game):
    print("You would like,", game)

main()


