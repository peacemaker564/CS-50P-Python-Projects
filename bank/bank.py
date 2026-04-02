def main():
    greeting = input("Greeting: ").strip()
    print(hello_eval(greeting))

def hello_eval(greet):
    if greet.lower().startswith("hello"):
        return 0
    elif greet.lower().startswith("h"):
        return 20

    else:
        return 100

if __name__ == "__main__":
    main()





