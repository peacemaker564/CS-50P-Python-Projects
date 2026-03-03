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
            # Requirements: Output ONLY the equation, no extra words
            print(f"{x} + {y} = {correct_sum}")

        count += 1

    # Requirements: Output format must be "Score: X"
    print(f"Score: {score}")

def get_level():
    while True:
        try:
            n = int(input("Level: "))
            if n in [1, 2, 3]:
                return n
        except ValueError:
            pass

def generate_integer(level):
    # Requirements: Returns a single randomly generated non-negative integer
    if level == 1:
        return random.randint(0, 9)
    elif level == 2:
        return random.randint(10, 99)
    elif level == 3:
        return random.randint(100, 999)
    else:
        raise ValueError("Invalid level")

if __name__ == "__main__":
    main()
