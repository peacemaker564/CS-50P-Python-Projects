def main():
    greeting = input("Greeting: ").strip()
    print(f"${value(greeting)}")

def value(greeting):
    if greeting.lower().startswith("hello"):
        return 100
    elif greeting.lower().startswith("h"):
        return 20
    else:
        return 0

if __name__ == "__main__":
    main()





