try:
    x = int(input("What's the x? "))


except ValueError:
    print("x is not an integer, dumbass.! Try again.")

print(f"x is {x}")
