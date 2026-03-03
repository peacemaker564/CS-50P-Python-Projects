#Generating ten math problems(x+y) on the basis of levels(1,2, and 3)
#Where 1 refers to single digit sums, 2 refers to double digit sums, and 3 to triple.

#Prompting the user to input the level, n.
#Using that level to determine the difficulty(level) of the problems.
#Using randint to generate random numbers, for both x and y.

#Saving the sum of the two numbers in to a variable.
#Prompting the user to provide the answer, and giving them three chances, and then displaying the answer if incorrect.
#If correct, moving onto the next question.
#After they are done answering all the questions, displaying the total score out of 10.

import random


def main():

    count = 0
    n = get_level()
    while count < 10:
        x, y = generate_integer(n)
        sum = x + y
        print(x, " + ", y , " = ", end="")
        user_answer = int(input(""))
        chances = 0
        while chances < 3:
            if user_answer == sum:
                    count = count + 1
                    score = score + 1
                    break

            else:
                print("EEE") #Mark of a wrong answer.
                chances =  chances + 1
                print(x, " + ", y , " = ", end="")

        else:
            print("Correct answer is: ", sum)


def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n not in [1,2,3]:
                continue
        except ValueError or TypeError:
            continue
        else:
            return n


def generate_integer(level):
    if level == 1:
       x = random.randint(0, 9)
       y = random.randint(0,9)

    elif level == 2:
        x = random.randint(10, 99)
        y = random.randint(10,99)
    else:
        x = random.randint(100, 999)
        y = random.randint(100,999)

    return x, y
    ...


if __name__ == "__main__":
    main()
