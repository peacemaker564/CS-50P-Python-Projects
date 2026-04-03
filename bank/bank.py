def main():
    greeting = input("Greeting: ").strip()
    print(f"${hello_eval(greeting)}")

def hello_eval(greet):
    if greet.lower().startswith("hello"):
        return 100
    elif greet.lower().startswith("h"):
        return 20
    else:
        return 0

if __name__ == "__main__":
    main()





