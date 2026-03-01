#This program lets the user guess the random generated number, between 1 & n, where n is the max range.

#Main algorithm:
#Extra: Also import randint from rando module.
#1. Asking the user for the number n in an integer input tab.
#2. Check if the user entered n is positive.
#3. Then use the randint function from random module to generate a number between 1 and n.
#4. Then prompting the user to guess that number, by taking positive integer inputs(repeat if user enters incorrect creds)
#5. Display where the user stands after they enter the value.(if its too large, or too small, or finally, they guessed it right.)


from random import randint

n = int(input("Level: "))

while not n > 0 :
    print("Please enter positive value.")
    n = int(input("Level: "))

guess = randint(1, n)
user_input = 0

while guess != user_input:
    #Use try and except to create a user entered value
    #check(should be positive, and do not accept anything other than digits.)

    while True:
             try:
                user_input = int(input("Guess: "))
                if not user_input > 0:
                    continue

             except ValueError:
                continue

             else:
                break


    if user_input < guess:
        print("Too small!")
    elif user_input > guess:
        print("Too large!")


print("Just right!")










