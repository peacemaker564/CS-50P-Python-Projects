import random

def main():
    count = 0
    n = get_level()
    score = 0

    while count < 10:
        chances = 0

        x = generate_integer(n)
        y = generate_integer(n)
        correct_sum = x + y

        while chances < 3:

            print(f"{x} + {y} = ", end="")
            try:
                user_answer = int(input(""))
                if user_answer == correct_sum:
                    score += 1
                    break
                else:
                    print("EEE")
                    chances += 1
            except ValueError:
                print("EEE")
                chances += 1
        else:

            print(f"{x} + {y} = {correct_sum}")

        count += 1


    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            continue

def generate_integer(level):

    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)

if __name__ == "__main__":
    main()
